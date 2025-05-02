import '@testing-library/jest-dom'
import { vi } from 'vitest'

// Prevent any call to window.alert from throwing
globalThis.alert = () => {}

// Stub fetch so onMount never rejects (and never resolves)
globalThis.fetch = () => new Promise(() => {})