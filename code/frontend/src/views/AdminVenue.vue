<script setup>
import router from "../router"
</script>
<template>
	<div class="venue">
		<div class="container">
			<div class="heading">Venues</div>
			<button class="btn btn-yellow" style="marginbottom: 20px">
				<router-link class="rlink" to="/adminaddvenue">
					+ Add Venue
				</router-link>
			</button>
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
				<template #cell(update)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click="routeUpdateVenue(row.item)"
					>
						Modify
					</b-button>
				</template>
				<template #cell(delete)="row">
					<b-button
						class="button btn btn-red"
						size="sm"
						@click="showDeletionModal(row.item.venue_id)"
					>
						Delete
					</b-button>
				</template>
				<template #cell(exportCSV)="row">
					<b-button
						class="button btn btn-yellow"
						size="sm"
						@click=" exportCSV(row.item)"
					>
						Export CSV
					</b-button>
				</template>
			</b-table>
			<b-modal
				v-model="show"
				id="delete-venue"
				title="Confirm venue deletion"
			>
				<p class="my-4">Are your sure you want to delete this venue?</p>
				<template #modal-footer>
					<b-button
						size="md"
						class="float-right btn btn-red"
						@click="show = false"
					>
						Cancel
					</b-button>
					<b-button
						size="md"
						class="float-right btn btn-yellow"
						@click="deleteVenue()"
					>
						Delete Venue
					</b-button>
				</template>
			</b-modal>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import { mapActions, mapGetters } from 'vuex';

export default {
	name: 'Venue',
	props: ['venue_id'],
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
				"BrowseMovies", "update","delete", "exportCSV"
			],
			items: [],
			show: false,
			selectedVenue: '',
		};
	},
	methods: {
		...mapActions(['loadVenue', 'routeModifyVenue']),
		...mapGetters(['getVenue', 'getAccessToken']),

		browse_movie(data){
			router.push(`/adminmovie/${data.venue_id}`)
		},
		exportCSV(data){
			function downloadBlob(content, filename, contentType) {
			// Creates a blob
				var blob = new Blob([content], { type: contentType });
				var url = URL.createObjectURL(blob);
				// Creates a link to download it
				var pom = document.createElement('a');
				pom.href = url;
				pom.setAttribute('download', filename);
				pom.click();
			}
			axios.get(`http://localhost:5000/exportcsv/${data.venue_id}`, {
				headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
			})
			.then((response) =>{
				downloadBlob(response.data, 'export.csv', 'text/csv;charset=utf-8;');
				alert('CSV exported successfully!');
			})
		},
		showDeletionModal(venue_id) {
			this.show = true;

			this.selectedVenue = venue_id;
			console.log(this.selectedVenue);
		},
		routeUpdateVenue(venueData) {
			this.routeModifyVenue(venueData);
			this.$router.push(`/adminmodifyvenue/${venueData.venue_id}`);
		},
		async deleteVenue() {
			await axios
				.delete(`http://localhost:5000/deletevenue/${this.selectedVenue}`, {
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${this.getAccessToken()}`
					},
				})
				.then(() => {
					alert('Venue deleted successfully!');
				})
				.catch(() => {
					alert('Error deleting venue!');
				});
			this.show = false;
			await this.reloadVenue();
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
