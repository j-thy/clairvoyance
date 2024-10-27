<script>
  import { router } from '@inertiajs/svelte'
	import { onMount } from 'svelte';
  export let events = undefined;
  import { inertia, Link } from '@inertiajs/svelte'
  import * as Table from "$lib/components/ui/table";

  // mounted() in VueJS / useEffect() in React
  onMount(() => {
    // We fire a partial reload to load the data in:
    router.reload({ only: ['events'] })
  })
  const previous = () => {
    router.visit("/events?page=2", {only: ['events'],})
  };
  const next = () => {
    router.visit("/events?page=3", {only: ['events'],})
  };
</script>
<!-- Make a div with dark class -->
<div class="relative flex min-h-screen flex-col dark">
  <Table.Root>
    <Table.Caption>Banner rateups.</Table.Caption>
    <a href="/events?page=2" use:inertia="{{ only: ['events'] }}">Show active</a>
    <Table.Header>
      <Table.Row>
        <Table.Head class="w-[100px]">Image</Table.Head>
        <Table.Head>Event</Table.Head>
        <Table.Head class="text-right">Region</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each events as event}
      <Table.Row>
        <Table.Cell><img src="/static/event_imgs/{event.image_file}" alt="sample 1" class="rounded-lg"></Table.Cell>
        <Table.Cell class="font-medium">{event.name}</Table.Cell>
        <Table.Cell class="text-right">{event.region}</Table.Cell>
      </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>
</div>
