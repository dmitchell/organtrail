var DoctorModel = Backbone.Model.extend({
	defaults: {
		id: null,
		name: "John Doe",
		waitTime: 30, // days to be seen by doctor
		description: "A long string to show as description--narrative.",
		rating: 78, // quality of care, i.e. likeliness he'll bump you up the list
		cost: 0.2, // money cost of seeing doctor
	}
});

var Doctors = Backbone.Collection.extend({
	url : "doctors",
	model : DoctorModel
});

// populates the table
var DoctorCollectionView = Backbone.View.extend({
	events: {
		"click a ": 'selectDoctor'
		},
	initialize: function() {
		this.template = _.template('<div class="row">' +
				'<a href="#" data-id="<%= model.get(\'id\') %>" data-dismiss="modal">' +
				'<div class="span6 doctor-pane">' +
   				'<h4 id="doctor-name"><%= model.get("name") %></h4>' +
    				'<table class="table table-condensed">' +
    					'<tbody>' +
    						'<tr><td rowspan="3" id="doctor-description" width="70%"><%= model.get("description") %></td>' +
    						'<td width="25%">Waiting List</td>' +
    						'<td id="doctor-waitTime" width="5%"><%= model.get("waitTime") %></td></tr>' +
    						'<tr><td>Success Rate</td><td class="id-rating">75%</td></tr>' +
    						'<tr><td>Cost</td><td id="doctor-cost"><%= model.get("cost") %></td></tr>' +
    						'</tbody>' +
    				'</table>' +
    			'</div>' +
    		'</div>');
    	},
	render : function() {
		this.$el.html('');
		for (var i = 0; i < this.collection.length; i++) {
			this.$el.append(this.template({index : i, model : this.collection.at(i)}));
		}
	},
	selectDoctor: function(event) {
		window.recipients.get(window.currentPlayer).save( {'doctor' : parseInt($(event.currentTarget).data('id')) },
				{ success : function() {
					// start the waiting room
					window.state = new GameState();
				}});
	}
})