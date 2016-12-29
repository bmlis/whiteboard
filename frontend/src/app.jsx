import styles from './index.scss';
import {List, ListItem} from 'material-ui/List';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import React from 'react';
import config from 'config';

/* const serverURL = "http://localhost:5000";*/

export default class App extends React.Component {
    state = {
        workouts: []
    }

    reloadWorkouts = () => {
        fetch(
            `${config.serverURL}/workouts`
        ).then(
            (response) => response.json()
        ).then(
            (json) => JSON.parse(json)
        ).then(
            (data) => this.setState({workouts: data.items})
        )
    }

    componentDidMount() {
        this.reloadWorkouts()
    };

    render() {
        return (
            <MuiThemeProvider>
                <div>
                    <WorkoutList workouts={this.state.workouts} />
                    <WorkoutForm reloadWorkouts={this.reloadWorkouts} />
                </div>
            </MuiThemeProvider>
        )
    }
}


class WorkoutForm extends React.Component {
    state = {
        activity_type: '',
    };

    handleSubmit = (event) => {
        event.preventDefault();
        fetch(`${config.serverURL}/workouts`,{
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'activity_type': this.state.activity_type})

        }).then((response) => this.props.reloadWorkouts())
    };

    handleActivityTypeChange = (event) => {
        this.setState({activity_type: event.target.value})
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <TextField
                        hintText="Activity type"
                        floatingLabelText="ActivityType"
                        value={this.state.activity_type}
                        onChange={this.handleActivityTypeChange}
                    /><br />
                    <div>
                        <RaisedButton
                            label="Submit"
                            style={{margin: 12}}
                            type="submit"
                        />
                    </div>
                </form>
            </div>
        )
    }
}

class WorkoutList extends React.Component {
    render() {
        const workouts = this.props.workouts.map(
            (workout) => {
                return (
                    <ListItem
                        key={workout.id}
                        primaryText={workout.activity_type}
                    />
                )
            }
        )
        return (<List>{workouts}</List>)
    }
}
