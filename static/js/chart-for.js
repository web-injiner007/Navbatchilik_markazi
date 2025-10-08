const ctx = document.getElementById('deviceChart');

    // 📍 Viloyatlar ro‘yxati
    const viloyatlar = [
      "Toshkent", "Samarqand", "Farg‘ona", "Andijon",
      "Namangan", "Buxoro", "Xorazm", "Navoiy",
      "Qashqadaryo", "Surxondaryo", "Sirdaryo", "Jizzax"
    ];

    // Har bir viloyatda jami qurilmalar soni
    const jami = [14, 10, 8, 5, 10, 7, 3, 2, 7, 11, 12, 13];
    // Ishlayotganlar soni
    const ishlayotgan = [5, 2, 4, 2, 4, 2, 1, 3, 6, 5, 4, 8];

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: viloyatlar,
        datasets: [
          {
            label: 'Ishlamayotgan qurilmalar',
            data: ishlayotgan,
            backgroundColor: '#2c3e50', // yashil
            borderRadius: 8,
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            ticks: { font: { size: 12 } }
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Ishlamayotgan qurilmalar soni'
            }
          }
        },
        plugins: {
          legend: { display: false },
          title: {
            display: true,
            text: 'Viloyatlar kesimida ishlamayotgan atslar statistikasi'
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                const index = context.dataIndex;
                const ishlay = ishlayotgan[index];
                const jamiQ = jami[index];
                const foiz = ((ishlay / jamiQ) * 100).toFixed(1);
                return `${ishlay} ta ishlayapti (${foiz}%)`;
              }
            }
          }
        }
      }
    });

      const ctxEmployees = document.getElementById('employeeChart');

    // 📍 Viloyatlar ro‘yxati
    const viloyatlarXodim = [
      "Andijon", "Termiz", "O'rikzor", "Xorazm",
      "Nukus", "Chig'atoy", "Qalqon", "Samarqand", "Navoiy", "Trassa"
    ];

    // 📊 Samaradorlik foizlari
    const samaradorlik = [55, 30, 47, 25, 60, 18, 30, 23, 15, 27];

    new Chart(ctxEmployees, {
      type: 'bar',
      data: {
        labels: viloyatlarXodim,
        datasets: [{
          label: 'Samaradorlik (%)',
          data: samaradorlik,
          backgroundColor: function(ctx) {
            const v = ctx.raw;
            if (v >= 90) return '#2c3e50';   // yashil
            if (v >= 80) return '#2c3e50';   // sariq
            return '#2c3e50';                // qizil
          },
          borderRadius: 8,
          barThickness: 25
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        indexAxis: 'y', // ✅ horizontal chart!
        scales: {
          x: {
            beginAtZero: true,
            max: 100,
            title: {
              display: true,
              text: 'Samaradorlik (%)'
            }
          },
          y: {
            ticks: {
              font: { size: 13 },
              color: '#333'
            }
          }
        },
        plugins: {
          legend: { display: false },
          title: {
            display: true,
            text: 'Batalyonlar kesimida eng yaxshi navbatchilik yurutuvchilar',
            font: { size: 16 }
          },
          tooltip: {
            callbacks: {
              label: (ctx) => `${ctx.parsed.x}% samaradorlik`
            }
          }
        }
      }
    });


    const sendBtn = document.getElementById('sendBtn');
    const messageInput = document.getElementById('messageInput');
    const chatBody = document.getElementById('chatBody');

    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') sendMessage();
    });

    function sendMessage() {
      const text = messageInput.value.trim();
      if (!text) return;

      const msg = document.createElement('div');
      msg.classList.add('message', 'user');
      msg.textContent = text;
      chatBody.appendChild(msg);

      messageInput.value = '';
      chatBody.scrollTop = chatBody.scrollHeight;

      // Ixtiyoriy javob (bot yoki boshqa foydalanuvchi)
      setTimeout(() => {
        const reply = document.createElement('div');
        reply.classList.add('message', 'other');
        reply.textContent = "Xabar qabul qilindi ✅";
        chatBody.appendChild(reply);
        chatBody.scrollTop = chatBody.scrollHeight;
      }, 800);
    }