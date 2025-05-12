
fetch('/dashboard_academy.csv')
  .then(response => response.text())
  .then(data => {
    const rows = data.trim().split('\n').slice(1);
    let table = '<table><thead><tr><th>Usuario</th><th>Firma</th><th>Labs</th><th>XP</th><th>Nivel</th><th>Insignias</th></tr></thead><tbody>';
    rows.forEach(row => {
      const cols = row.split(',');
      const nivel = cols[4].trim().split(' ')[1];
      const roles = cols[6] ? cols[6].trim().split(';') : [];

      const nivelBadge = `<img src="/assets/badges/badge-nivel-${nivel}.svg" alt="Nivel ${nivel}" style="height: 60px;">`;
      const roleBadges = roles.map(r => 
        `<img src="/assets/badges/badge-role-${r.trim()}.svg" alt="${r}" style="height: 50px; margin-left: 4px;">`
      ).join(' ');

      table += `<tr>
        <td>${cols[0]}</td>
        <td>${cols[1]}</td>
        <td>${cols[2]}</td>
        <td>${cols[3]}</td>
        <td>${nivelBadge}</td>
        <td>${roleBadges}</td>
      </tr>`;
    });
    table += '</tbody></table>';
    document.getElementById('leaderboard-table').innerHTML = table;
  });
