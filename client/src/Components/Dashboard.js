import { useState, useEffect } from "react";
import useAuth from "./utility/useAuth";
import Player from "./Player";
import TrackSearchResult from "./TrackSearchResult";
import "./css/Dashboard.css";
import SpotifyWebApi from "spotify-web-api-node";

import { useDataLayerValue } from "./DataLayer";
import Header from "./Header";

const spotify = new SpotifyWebApi({
  clientId: "c0f037a261fd4f649bc7ca1338b5a3e0",
});

export default function Dashboard({ code }) {
  const [{ token, searchResults }, dispatch] = useDataLayerValue();
  const accessToken = useAuth(code);
  useEffect(() => {
    if (accessToken) {
      dispatch({
        type: "SET_TOKEN",
        token: accessToken,
      });
      spotify.setAccessToken(accessToken);
      spotify.getMe().then((user) => {
        dispatch({
          type: "SET_USER",
          user: user,
        });
      });
    }
  }, [accessToken, dispatch]);

  const [playingTrack, setPlayingTrack] = useState();
  const [lyrics, setLyrics] = useState("");

  function chooseTrack(track) {
    setPlayingTrack(track);
    dispatch({
      type: "SET_SEARCH_RESULTS",
      searchResults: [],
    });
    setLyrics("");
  }

  const flask_url = "http://127.0.0.1:5000"; //https://ani-oke-flask-server.herokuapp.com
  //
  var htmlObject = document.createElement("div");
  useEffect(() => {
    if (!token) return;
    spotify.setAccessToken(token);
  }, [token]);
  useEffect(() => {
    console.log(playingTrack);
    if (!playingTrack) return;
    const tmp = playingTrack.title + playingTrack.artist;
    fetch(`${flask_url}/getdata/${tmp}`)
      .then(function (response) {
        return response.json();
      })
      .then(function (text) {
        console.log("GET response text:");
        console.log(text);
        setLyrics(text);

        htmlObject.innerHTML = lyrics.ly;
      });
  }, [playingTrack]);

  return (
    <div className="main-dashboard">
      <Header spotify={spotify}></Header>
      <div className="body">
        {searchResults.map((track) => (
          <TrackSearchResult
            track={track}
            key={track.uri}
            chooseTrack={chooseTrack}
          />
        ))}

        {searchResults.length === 0 && (
          <div
            className="text-center"
            style={{ whiteSpace: "pre" }}
            dangerouslySetInnerHTML={{ __html: lyrics.ly }}></div>
        )}
      </div>
      <div>
        <Player accessToken={token} trackUri={playingTrack?.uri} />
      </div>
    </div>
  );
}
