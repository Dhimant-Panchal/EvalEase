<script lang="ts">
    import { ClickableTile } from "carbon-components-svelte";

    export let code = "";
    export let title = "";
    export let href = "";
</script>

<ClickableTile {href} data-sveltekit-preload-data="hover">
    <h5>{code}</h5>
    <h7>{title}</h7>
</ClickableTile>
