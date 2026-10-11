import { Suspense } from "react";
import { createClient } from "@/lib/supabase/server";

export default function Home() {
  return (
    <main style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>RPI Men's Club Soccer Stats</h1>
      <h2>Team Roster</h2>

      <Suspense fallback={<p>Loading players...</p>}>
        <PlayerRoster />
      </Suspense>
    </main>
  );
}

async function PlayerRoster() {
  const supabase = await createClient();

  const { data: players, error } = await supabase
    .from("players")
    .select("id, full_name, jersey_number, position")
    .order("full_name");

  if (error) {
    return <p>Database error: {error.message}</p>;
  }

  if (!players || players.length === 0) {
    return <p>No players found. Add players in Supabase.</p>;
  }

  return (
    <ul>
      {players.map((player) => (
        <li key={player.id}>
          #{player.jersey_number ?? "—"} {player.full_name}
          {player.position ? ` — ${player.position}` : ""}
        </li>
      ))}
    </ul>
  );
}