var GameState = Backbone.Model.extend({
	defaults : {
		state : "staging-room",
		players : window.recipients,
		donorPool : 0.2,
		timeRemaining : 0
	},
	urlRoot : function() {
		return "state/" + this.get('state');
	},
	initialize : function() {
		$('#stagingModal').modal('show');
		$(".btn-primary").on('click', this, this.sendMove);
		this.pollWaitingRoom(this);
	},
	pollWaitingRoom : function(state) {
		state.fetch({
			success : this.waitingRoom
		});
	},
	waitingRoom : function(state) {
		window.recipients.reset(state.get('players'));
		if (state.get('state') === "staging-room") {
			window.setTimeout(function() { 
				state.pollWaitingRoom(state);
			}, 
			1000);
		}
		else {
			console.log(state.get('state'));
			$('#stagingModal').modal('hide');
		}
	},
	sendMove : function(event) {
		var cacheThis = event.data;
		$.getJSON('mechanics/' + window.currentPlayer + '/' + $(event.currentTarget).data('id'), {}, 
				function(data) {
					// TODO tell the user if it was successful (data.result)
					// update donor pool
					var dbar = $("#donor-bar");
					dbar.width(data.donorPool + "%");
					dbar.html(data.donorPool + "%");
					// update rankings
					window.recipients.reset(data.players);
			        // update state
					cacheThis.set('state', data.state);
		});
	}
});

