<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import router from './router/router';

export default {
  name: 'App',
  router
}
</script>
