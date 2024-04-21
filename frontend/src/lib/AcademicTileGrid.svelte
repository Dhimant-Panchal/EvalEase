<div class="acad-grid-wrapper">
    <slot />
</div>

<style>
    .acad-grid-wrapper {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: var(--cds-spacing-02);
    }

    @media (width <= 1200px) {
        .acad-grid-wrapper {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    @media (width <= 600px) {
        .acad-grid-wrapper {
            grid-template-columns: repeat(1, 1fr);
        }
    }
</style>
