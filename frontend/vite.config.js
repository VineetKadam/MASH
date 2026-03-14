import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite' // 1. Import the Tailwind plugin

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(), // 2. Add it to the plugins array
  ],
  css: {
    // 3. Optional: In Vite 8, forcing 'postcss' as the transformer 
    // prevents internal conflicts between Vite's and Tailwind's CSS engines.
    transformer: 'postcss', 
  }
})