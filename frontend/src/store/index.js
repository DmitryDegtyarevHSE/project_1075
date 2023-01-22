import {createStore} from 'vuex';

export default createStore({
	state: () =>  ({
		tickets: [],
		user: null,
		filterHelpType: []
	}),
	mutations: {
		setFetchedTickets(state, tickets) {
			state.tickets = tickets
		},
		setNewTicketStatusById(state, element){
			state.tickets.find((ticket) => ticket.id === element.elementId).status = element.newStatus
		},
		setUser(state, user) {
			state.user = user
		}
	},
	actions: {
		async getUser(ctx) {
			const ans = await fetch('https://dfvrn.pythonanywhere.com/api/user', {method: 'GET'})
			const res = await ans.json()
			ctx.commit('setUser', res)
		},
		async fetchTickets(ctx) {
			try {
				const ans = await fetch('https://dfvrn.pythonanywhere.com/api/appeal', {method: 'GET'})
				const res = await ans.json()
				ctx.commit('setFetchedTickets', res)
			} catch (e) {
				console.error(`Error during fetch in mount: ${e}`)
			}
		},
		async patchTicketStatusById(ctx, element) {
			const cookie = document.cookie
			ctx.commit('setNewTicketStatusById', element)
			await fetch(`https://dfvrn.pythonanywhere.com/api/appeal/${element.elementId}`, {
				method: 'PATCH',
				headers: {
					'Content-Type': 'application/json',
					'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
				},
				body: JSON.stringify({
					'status': element.newStatus
				})
			})
		},
		async patchTicketNotes(ctx, element, newNote) {
			const cookie = document.cookie
			if (element.notes !== newNote) {
				await fetch(`https://dfvrn.pythonanywhere.com/api/appeal/${element.id}`, {
					method: 'PATCH',
					headers: {
						'Content-Type': 'application/json',
						'X-CSRFToken': cookie.substring(cookie.indexOf('csrftoken=') + 10)
					},
					body: JSON.stringify({
						'notes': newNote
					})
				})
			}
		},
	}
})
