var GameState = Backbone.Model.extend({
	defaults : {
		state : "waiting-room",
		players : window.recipients,
		donorPool : 0.2,
		timeRemaining : 0
	},
	urlRoot : function() {
		return "state/" + this.get('state');
	},
	initialize : function() {
		this.pollWaitingRoom(this);
	},
	pollWaitingRoom : function(state) {
		state.fetch({
			success : this.waitingRoom
		});
	},
	waitingRoom : function(state) {
		window.recipients.reset(state.get('players'));
		if (state.get('state') === "waiting-room") {
			window.setTimeout(function() { 
				state.pollWaitingRoom(state);
			}, 
			1000);
		}
		else {
			console.log(state.get('state'));
			state.getMove();
		}
	},
	getMove : function() {
		
	}
});

