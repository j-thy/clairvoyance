<script>
  import { router } from '@inertiajs/svelte'
	import { onMount } from 'svelte';
  import { inertia, Link } from '@inertiajs/svelte'
  import * as Table from "$lib/components/ui/table";
  import { Button } from "$lib/components/ui/button/index.js";
  import { toast } from "svelte-sonner";

  // Get events from props
	let { events = undefined, num_pages = undefined } = $props();

  // Get current page number from URL
  const urlParams = new URLSearchParams(window.location.search);
  const isPageNum = urlParams.has('page');
  let page = isPageNum ? parseInt(urlParams.get('page')) : 1;

  // mounted() in VueJS / useEffect() in React
  onMount(() => {
    // We fire a partial reload to load the data in:
    // If events is undefined, we reload the page
    if (events === undefined) {
      router.reload({ only: ['events', 'num_pages'] })
      console.log("Mounted");
    }
  })

  const previous = () => {
    if (page-1 > 0) {
      router.visit(`/events?page=${page-1}`, { only: ['events'] });
      console.log("Previous");
    }
    else {
      toast("You are at the first page")
    }
  };
  const next = () => {
    if (page+1 <= num_pages) {
      router.visit(`/events?page=${page+1}`, { only: ['events'] });
      console.log("Next");
    }
    else {
      toast("You are at the last page")
    }
  };
</script>
<!-- Make a div with dark class -->
<Button onclick={previous}>Previous</Button>
<Button onclick={next}>Next</Button>
<div class="relative flex min-h-screen flex-col dark">
  <Table.Root>
    <Table.Caption>Banner rateups.</Table.Caption>
    <a href="/events?page=1" use:inertia="{{ only: ['events'] }}">Show active</a>
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
