<template>
  <div class="p-6 relative">
    <!-- Resultado del dado -->
    <div
      v-if="rolledResult !== null"
      class="result-display"
    >
      🎲 {{ rolledResult }}
    </div>

    <!-- Contenedor del dado -->
    <div ref="sceneContainer" class="scene-container mt-10"></div>

    <!-- Botón para lanzar el dado -->
    <button @click="rollDice" class="roll-button">
      Lanzar Dado
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import gsap from 'gsap'

const sceneContainer = ref(null)
const rolledResult = ref(null)

let scene, camera, renderer, icosahedron, controls, faceNormals = []

const initScene = () => {
  scene = new THREE.Scene()
  scene.background = null // Fondo transparente

  const containerWidth = sceneContainer.value.clientWidth
  const containerHeight = sceneContainer.value.clientHeight

  camera = new THREE.PerspectiveCamera(75, containerWidth / containerHeight, 0.1, 1000)
  camera.position.z = 5

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true }) // Soporte para fondo transparente
  renderer.setSize(containerWidth, containerHeight)
  sceneContainer.value.appendChild(renderer.domElement)

  const geometry = new THREE.IcosahedronGeometry(1, 0)

  const material = new THREE.MeshBasicMaterial({
    color: '#005f99',
    flatShading: true
  })

  icosahedron = new THREE.Mesh(geometry, material)

  const edges = new THREE.EdgesGeometry(geometry)
  const lineMaterial = new THREE.LineBasicMaterial({ color: 0x66ccff })
  const wireframe = new THREE.LineSegments(edges, lineMaterial)
  icosahedron.add(wireframe)

  scene.add(icosahedron)

  computeFaceNormals(geometry)
  addFaceNumbers(geometry)

  controls = new OrbitControls(camera, renderer.domElement)
  controls.enabled = false

  animate()
}

const computeFaceNormals = (geometry) => {
  const positions = geometry.attributes.position
  faceNormals = []

  for (let i = 0; i < positions.count; i += 3) {
    const a = new THREE.Vector3().fromBufferAttribute(positions, i)
    const b = new THREE.Vector3().fromBufferAttribute(positions, i + 1)
    const c = new THREE.Vector3().fromBufferAttribute(positions, i + 2)
    const ab = new THREE.Vector3().subVectors(b, a)
    const ac = new THREE.Vector3().subVectors(c, a)
    const normal = new THREE.Vector3().crossVectors(ab, ac).normalize()
    faceNormals.push(normal)
  }
}

const animate = () => {
  requestAnimationFrame(animate)
  renderer.render(scene, camera)
  controls.update()
}

const rollDice = () => {
  const faceIndex = Math.floor(Math.random() * faceNormals.length)
  const targetNormal = faceNormals[faceIndex].clone()
  const targetQuaternion = new THREE.Quaternion().setFromUnitVectors(targetNormal, new THREE.Vector3(0, 0, 1))

  const randomRotX = Math.PI * 2 * (2 + Math.random() * 2)
  const randomRotY = Math.PI * 2 * (2 + Math.random() * 2)
  const randomRotZ = Math.PI * 2 * (2 + Math.random() * 2)

  gsap.to(icosahedron.rotation, {
    x: icosahedron.rotation.x + randomRotX,
    y: icosahedron.rotation.y + randomRotY,
    z: icosahedron.rotation.z + randomRotZ,
    duration: 2,
    ease: "power2.out",
    onComplete: () => {
      const dummy = new THREE.Object3D()
      dummy.setRotationFromQuaternion(targetQuaternion)

      gsap.to(icosahedron.rotation, {
        x: dummy.rotation.x,
        y: dummy.rotation.y,
        z: dummy.rotation.z,
        duration: 1,
        ease: "bounce.out",
        onComplete: () => {
          rolledResult.value = faceIndex + 1
        }
      })
    }
  })
}

const addFaceNumbers = (geometry) => {
  const positions = geometry.attributes.position

  for (let i = 0; i < positions.count; i += 3) {
    const a = new THREE.Vector3().fromBufferAttribute(positions, i)
    const b = new THREE.Vector3().fromBufferAttribute(positions, i + 1)
    const c = new THREE.Vector3().fromBufferAttribute(positions, i + 2)
    const center = new THREE.Vector3().addVectors(a, b).add(c).divideScalar(3)

    const ab = new THREE.Vector3().subVectors(b, a)
    const ac = new THREE.Vector3().subVectors(c, a)
    const normal = new THREE.Vector3().crossVectors(ab, ac).normalize()

    const number = i / 3 + 1

    const canvas = document.createElement('canvas')
    canvas.width = 128
    canvas.height = 128
    const ctx = canvas.getContext('2d')

    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = 'white'
    ctx.font = 'bold 72px Arial'
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillText(number.toString(), canvas.width / 2, canvas.height / 2)

    const texture = new THREE.CanvasTexture(canvas)
    const material = new THREE.MeshBasicMaterial({ map: texture, transparent: true })
    const plane = new THREE.Mesh(new THREE.PlaneGeometry(0.6, 0.6), material)

    plane.position.copy(center.clone().add(normal.clone().multiplyScalar(0.001)))

    const quaternion = new THREE.Quaternion().setFromUnitVectors(
      new THREE.Vector3(0, 0, 1),
      normal
    )
    plane.quaternion.copy(quaternion)

    icosahedron.add(plane)
  }
}

onMounted(async () => {
  await nextTick()
  initScene()
})
</script>

<style scoped>
  @import '@/assets/css/diceStyles/diceStyle-1.css';
</style>
