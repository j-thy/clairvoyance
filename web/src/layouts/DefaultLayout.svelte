<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { DarkMode } from 'flowbite-svelte';
</script>
<Navbar>
  <DarkMode />
  <NavBrand href="/">
    <img src="/static/imgs/ClairvoyanceLogo.svg" class="me-3 h-6 sm:h-9" alt="Clairvoyance" />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Clairvoyance</span>
  </NavBrand>
  <NavHamburger  />
  <NavUl >
    <NavLi href="/">Home</NavLi>
    <NavLi href="/events">Events</NavLi>
  </NavUl>
</Navbar>

<body class="bg-white dark:bg-gray-800 dark:text-white">
    <div><slot></slot></div>
</body>