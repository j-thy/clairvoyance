<script>
    import { Alert } from 'flowbite-svelte';
    export let events;
    let counter = 0;
    let incCounter = () => counter++;
</script>
<div class="p-8">
  <Alert>
    <span class="font-medium">Info alert!</span>
    Change a few things up and try submitting again.
  </Alert>
</div>
<p>Hello from Svelte!
    <span style="color: transparent">
        <span class="text-blue-500">and Tailwind!</span>
    </span>
    <button on:click={incCounter}>Counter: {counter}</button>
</p>
<ul>
    {#each events as event}
        <li>{event.name}</li>
    {/each}
</ul>