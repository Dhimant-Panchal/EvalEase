<script>
    import Mast from "$lib/Mast.svelte";
    import {
        FluidForm,
        TextInput,
        PasswordInput,
        Button,
    } from "carbon-components-svelte";
</script>

<Mast title="Login" strapline="Enter your 365 credentials below.">
    <FluidForm method="POST">
        <TextInput
            name="username"
            labelText="User name"
            placeholder="Enter user name..."
            required
        />
        <PasswordInput
            required
            type="password"
            name="password"
            labelText="Password"
            placeholder="Enter password..."
        />
        <Button type="submit">Login</Button>
    </FluidForm>
</Mast>
