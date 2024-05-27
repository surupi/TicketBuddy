<template>
	<div id="app">
		<Header />
		<router-view />
		<Footer />
	</div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
	name: 'App',
	components: {
		Header,
		Footer,
	},
};
</script>

<style>
body {
	font-family: Poppins;
}
.router-link {
	color: #000;
	text-decoration: none;
}
</style>
