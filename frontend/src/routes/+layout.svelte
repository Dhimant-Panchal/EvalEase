<script lang="ts">
    import "carbon-components-svelte/css/all.css";

    import {
        Header,
        SkipToContent,
        Content,
        HeaderUtilities,
        HeaderActionLink,
    } from "carbon-components-svelte";
    import VirtualColumnKey from "carbon-icons-svelte/lib/VirtualColumnKey.svelte";
    import Home from "carbon-icons-svelte/lib/Home.svelte";

    // TODO: PageData type is broken? Type 'never'???
    export let data: {
        name?: string;
    };
</script>

<Header company="UOS" platformName="Marking Moderation System">
    <svelte:fragment slot="skip-to-content">
        <SkipToContent />
    </svelte:fragment>
    <HeaderUtilities>
        {#if data?.name}
            <div
                style="display:flex; align-items:center; justify-content:center; padding-right: 8px; user-select: none;"
            >
                <span style="display: block; color: #fff"> {data?.name} </span>
            </div>
        {/if}
        <HeaderActionLink
            href="/auth"
            aria-label="Auth"
            icon={VirtualColumnKey}
        />
        <HeaderActionLink href="/" aria-label="Home" icon={Home} />
    </HeaderUtilities>
</Header>

<Content>
    <slot />
</Content>

<style>
    @media (width <= 600px) {
        /* TODO: Broken on auth screen. */
        :global(main) {
            padding-left: 0 !important;
            padding-right: 0 !important;
            overflow-x: hidden;
        }
    }
</style>
