<script setup>
import router from "../router"
</script>

<template>
	<div class="venue">
		<div class="container">
			<h5>Search for venues based on Venue State: </h5>
            <br>
			<div>
				<form class="form-inline my-2 my-lg-0" @submit.prevent="searchvenue">
				<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" v-model="selectedVenue">
				<br>
				<input class="btn btn-outline-success my-2 my-sm-0" type="submit" value="Search">
				</form>
			</div>
			<br>
			<b-table class="border-top" striped :items="items" :fields="fields">
				<template #cell(BrowseMovies)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click=" browse_movie(row.item)"
					>
						Browse Movies
					</b-button>
				</template>
			</b-table>
		</div>
	</div>
</template>


<script> 
import { mapActions, mapGetters } from "vuex";

export default {
	name: 'Venue',
	data() {
		return {
			fields: [
			{
					key: 'venue_id',
					label: 'Venue ID',
					class: 'text-center',
				},
				{
					key: 'venue_name',
					label: 'Venue Name',
					class: 'text-center',
				},
				{
					key: 'venue_state',
					label: 'Venue State',
					class: 'text-center',
				},
				{
					key: 'venue_city',
					label: 'Venue City',
					class: 'text-center',
				},
				"BrowseMovies"
			],
			items: [],
			show: false,
			selectedVenue: '',
		};
	},
	methods: {
		...mapActions(['loadVenue']),
		...mapGetters(['getVenue', 'getAccessToken']),
		searchvenue(){
			fetch(`http://127.0.0.1:5000/search_venue_keyword/${this.selectedVenue}` , 
			{
				headers: {"Content-Type":"application/json",
				Authorization: `Bearer ${this.getAccessToken()}`}}

			)
			.then(x => x.json())
			.then(data => {this.items = data})
		},
		browse_movie(data){
			router.push(`/pickmovie/${data.venue_id}`)
		},
		async reloadVenue() {
			await this.loadVenue();
			this.items = await this.getVenue();
		},
	},
	async mounted() {
		await this.reloadVenue();
	},
};
</script>

<style scoped>
.venue {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 20px;
}
.button {
	margin-right: 10px;
}
.btn-yellow {
	background-color: #e4c314 !important;
	color: #000 !important;
	font-weight: 600;
}
.btn-red {
	background-color: #ff918d;
	color: #000;
	font-weight: 600;
}
.rlink {
	color: #000;
	text-decoration: none;
}
</style>
