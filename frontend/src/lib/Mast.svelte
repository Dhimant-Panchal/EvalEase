<script>
    import { Column, Grid, Row } from "carbon-components-svelte";

    export let title = "Hello World";
    export let strapline = "Some longer text and description here.";
</script>

<Grid>
    <Row>
        <Column>
            <h1>{title}</h1>
            <p style="margin-bottom: var(--cds-layout-03)">{strapline}</p>
        </Column>
    </Row>
    <Row>
        <Column>
            <slot />
        </Column>
    </Row>
</Grid>
