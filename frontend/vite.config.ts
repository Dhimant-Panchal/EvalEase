import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			// https://kit.svelte.dev/docs/faq#how-do-i-use-x-with-sveltekit-how-do-i-use-a-different-backend-api-server.
			"/api": {
				target: "http://localhost:8000/",
				changeOrigin: true,
			},
		}
	}
});
