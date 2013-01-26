var GameState = Backbone.Model.extend({
	defaults : {
		state : "waiting-room",
		players : window.recipients,
		donorPool : 0.2
	},
	urlRoot : function() {
		return "/state/" + this.state;
	},
	initialize : function() {
		this.pollWaitingRoom();
	},
	pollWaitingRoom : function() {
		this.fetch({
			success : this.waitingRoom
		})
	}
	waitingRoom : function(state) {
		window.recipients.updateState(state.players);
		if (state.state === "waiting-room") {
			window.setTimeout(this.pollWaitingRoom, 1000);
		}
		else this.getMove();
	}
});

