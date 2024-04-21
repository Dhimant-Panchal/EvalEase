import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions = {
	default: async ({ cookies, request, fetch }) => {
		const formData = await request.formData();

		const res = await fetch("/api/auth/", {
			method: "POST",
			body: formData,
		})

		if (res.ok) {
			const token = (await res.json())["token"];
			cookies.set("token", token, {
				path: "/"
			});
			redirect(302, "/");
		}

		return fail(500);
	},
} satisfies Actions;