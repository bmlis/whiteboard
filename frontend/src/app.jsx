import styles from './index.scss';
import {List, ListItem} from 'material-ui/List';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import React from 'react';

const serverURL = "backend";

export default class App extends React.Component {
    state = {
        workouts: []
    }

    componentDidMount() {
        console.log(`${serverURL}/workouts`);
        fetch(`${serverURL}/workouts`).then(
            (response) => {
                // should be json
                return response; // .json();
            }
        ).then(
            (data) => {
                console.log(data);
                this.setState({
                    workouts: data.items
                })
            }
        )
    };

    render() {
        return (
            <MuiThemeProvider>
                <div>
                    <WorkoutList workouts={this.state.workouts} />
                    <WorkoutForm />
                </div>
            </MuiThemeProvider>
        )
    }
}


class WorkoutForm extends React.Component {
    state = {
        open: false,
    };

    handleSubmit = (event) => {
        event.preventDefault();
    };

    render() {
        const items = ["dupa"];
        const buttonStyle = {
            margin: 12
        }
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <TextField
                        hintText="Activity type"
                        floatingLabelText="ActivityType"
                    /><br />
                    <div>
                        <RaisedButton
                            label="Default"
                            style={buttonStyle}
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
