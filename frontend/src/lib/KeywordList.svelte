<script lang="ts">
    import { Tag } from "carbon-components-svelte";

    export let selection: string[] = [];

    export let filter = false;
</script>

{#if selection.length > 0}
    <div
        style="padding: var(--cds-spacing-04); background-color: var(--cds-ui-02)"
    >
        {#each selection as kw}
            <Tag
                type="blue"
                bind:filter
                on:close={() => (selection = selection.filter((o) => o != kw))}
                >{kw}</Tag
            >
        {/each}
    </div>
{/if}
