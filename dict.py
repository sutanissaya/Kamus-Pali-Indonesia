import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Kamus Pāḷi-Indonesia", page_icon="🪷")

st.markdown("<h1 style='text-align: center;'>🪷Kamus Pāḷi-Indonesia 🪷</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>berdasarkan <em>Concise Pali-English Dictionary</em> oleh A. P. Buddhadatta (1992)</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>terjemahan oleh SuttaCentral</h3>", unsafe_allow_html=True)
st.divider()

st.sidebar.write("Tampilkan kamus di [SuttaCentral](https://suttacentral.net/define/a%E1%B9%81sa?lang=id)")
st.sidebar.write("Unduh [Kamus Pāḷi-Indonesia (JSON)](https://github.com/suttacentral/sc-data/blob/main/dictionaries/simple/id/pli2id_cped.json)")

st.sidebar.divider()

st.sidebar.write("Kami berusaha untuk memperbaiki dan mengembangkan situs web ini. Jika Anda memiliki saran atau ide, kami akan menerimanya dengan senang hati melalui [email](mailto:sutanissaya@gmail.com).")
st.sidebar.write("_Karya di situs web berlisensi di bawah [CC0-1.0 Universal](https://github.com/sutanissaya/palijuncturesplitter/blob/main/LICENSE). Anda dipersilahkan untuk mengembangkan, memodifikasi, memasukkan ke dalam karya lain, menggunakan kembali, dan mendistribusikan sebebas mungkin dalam bentuk apa pun dan untuk tujuan apa pun, termasuk namun tidak terbatas pada tujuan komersial._")





"""
aṁsa: m.  bahu (_aṁse karoti_  meletakkan di bahu, menyandang, memanggul, memikul); bagian, hal berbagi; sudut, penjuru, ujung, tepi; **~kūṭa**m. nt. pundak, bahu.\n
akallaka: a.  sakit, tak sehat.\n
akāmaka: a.  tak ingin, tak mau, tak sudi.\n
akiriya: a.  tidak praktis, tidak bijaksana, bodoh;  nt.  tanpa tindakan; non-aksi;  **~vāda**a. yang berpaham (yang dikemukakan _Pūraṇa-kassapa_) bahwa semua perbuatan tidak menghasilkan ganjaran; yang menganut paham tanpa-tindakan.\n
akuppa: a.  tak tergoyahkan, pasti, teguh, kokoh, aman, mantap.\n
akusala: a.  yang tidak bajik, buruk, jahat;  nt. keburukan, kejahatan.\n
akkamati: menginjak, menapaki, menghampiri, menyerang, menendang, menabrak, menerjang, melejang, bangkit.\n
akkosa: m.  memarahi, mencerca, memaki, mencaci.\n
akkosati: memarahi, mencaci-maki, menghardik, mengomeli, mengutuk, _mencerca_.\n
akkha: 1.  m. gandar atau as roda; 2. m. guli (kelereng, gundu); dadu; 3. a. bermata; **~dassa** m. seseorang yang mencermati (memeriksa) dadu; wasit; hakim; **~dhutta** m. pejudi.\n
akkhaka: m.  tulang leher.\n
akkhayita: a.  tak rusak, belum rusak, belum membusuk.\n
akkhara: a.  tetap, awet, tahan lama, abadi; nt. sg. suku kata, aksara, huruf; pl. suara, bunyi, nada, kata-kata, tulisan. [aksara ← Skt. akṣara]
akkharikā: f.  tebak huruf (aksara).\n
akkhāta :  (pp dari **akkhāti**) diumumkan, dinyatakan, dimaklumkan, diberitahu, ditunjukkan; kata kerja.\n
akkhāti: menyatakan, memaklumkan, mengumumkan, memberitahukan, mengutarakan, mengemukakan.\n
akkhāna: m.  hal mengisahkan, menceritakan; kisah, cerita, legenda, laporan, pemaparan, pengisahan; pengisah, pencerita, pemapar, pelapor.\n
akkhi: nt.  mata; **~rogin** a. berpenyakit mata, menderita penyakit mata.\n
agada: m. obat, antidot.\n
agāra: nt.  rumah atau pondok; (kehidupan be)rumah tangga.\n
agāriya: m.  umat awam, umat berumah tangga, perumah tangga; **anagāriyā**f. kehidupan tidak berumah tangga.\n
agga: a.  pertama, terdepan; tertinggi, terpuncak; terluhur; terbaik; termasyhur, terutama, kampiun; nt. puncak, titik, ujung; rumah (kecil), kediaman, naungan, pondok, ruang, aula; **~kārikā**pencoba pertama, pencicip (pengecap) pertama, contoh (sampel), uji-coba pertama; **~mahesī**f. permaisuri (istri raja yang utama).\n
aggañña: a.  yang tertinggi, terkemuka, terpenting.\n
aggi: m.  api, nyala api, lidah api, percikan (bunga) api, lautan api, kobaran api; api persembahan; Dewa Api Agni.\n
aggha: m.  harga, nilai. [harga/argo ← Skt. argha]
agghanaka: a.  bernilai, sama dengan, senilai.\n
agghāpeti: (kaus. dari **agghati**)  menilai, memberi harga.\n
aṅga: nt.  tungkai, anggota tubuh; bagian, anggota, unsur, faktor; tanda, ciri, atribut, kualitas, hal (**iminā p’aṅgena**karena inilah); urusan, kepentingan, minat; **~jāta**m.  “bagian pembeda”, diri pria atau wanita, alat kelamin; **~maṅgāni**semua anggota tubuh, sekujur badan..\n
aṅgaṇa: nt.  lapangan, halaman, pelataran, alun-alun, medan, arena, gelanggang; noda, noda batin.\n
aṅgāra: m. nt.  arang, bara (api); **~kaṭāha** m. nt. wadah bara api, anglo.\n
aṅgāraka: a.  seperti bara, berwarna merah.\n
aṅguṭṭha: m.  ibu jari, jempol.\n
aṅgula: m.  jari tangan atau jari kaki; ukuran satu jari (menurut Bhikkhu Thanissaro 1 **sugataṅgula** = 2,08 cm).\n
aṅgulī  (aṅguli): f.  jari; **~patodaka** menggamit (_nudging with the fingers_), menggelitik, menggilik-gilik; **~poṭha** _snapping or cracking the fingers_, memetik jari, menjentikkan jari.\n
accaya: m.  hal berlalu, lewat, hal melewati atau melampaui, mengatasi, menaklukkan; hal melanggar, pelanggaran; meninggal dunia, berakhir, mati; **accayena**setelah lewat, setelah meninggal dunia, setelah berakhir, setelah.\n
acci (accī): f.  nyala api, pijar, cahaya.\n
accha: 1. a. jernih, bening, tembus pandang, transparan; 2. m. beruang; 3. = **akkha**; 4. a. merusak, menyakitkan, jahat, buruk.\n
acchati: duduk, duduk diam; berdiam, tinggal menyendiri; berada, hidup.\n
accharā: 1.  f.  bidadari (yang melayani dewa dengan tarian dan nyanyian); 2.ujung jari dipertemukan, penjentikan jari, sekejap; **ekaccharakkhaṇe** dalam seketika; **~saṅghāta** memetik jari, menjentikkan jari (= **aṅgulipoṭhana**). [apsara ← Skt. apsarā]
acchariya: a. nt.  mengagumkan, luar biasa, hebat, mengherankan, aneh, dahsyat, mencengangkan, menakjubkan.\n
acchādeti: menutupi, mengenakan (busana), melingkupi, mengisi.\n
aja: m.  kambing (jantan);  **~pāla** penggembala kambing.\n
ajaka: m. kambing jantan; f.  **ajikā, ajiyā**.\n
ajātabuddhi: f.  hal masih lugu, belum memiliki kebijaksanaan intelektual.\n
ajina: nt.  kulit atau jangat antelop hitam yang dikenakan para petapa sebagai pakaian; **~kkhipa**nt.  jubah yang terbuat dari jalinan potongan/setrip kulit antelop hitam.\n
ajja: adv. hari ini, sekarang; **~tagge** adv.  mulai hari ini, sejak sekarang.\n
ajjhatta: a.  yang bersifat pribadi, yang berhubungan dengan diri sendiri, yang muncul dari dalam, batiniah;  **ajjhattaṁ**adv. secara pribadi, dari dalam, ke dalam (lawan dari lahiriah, ke luar).\n
ajjhācarati: berperilaku sesuai dengan, mencumbui, melanggar.\n
ajjhācāra: m.  perilaku atau tata laku remeh (sepele) (di luar parajika dan sangghadisesa); pelanggaran; cumbu-cumbuan; hubungan seksual.\n
ajjhāpajjati: melakukan pelanggaran, melanggar.\n
ajjhāvasati: menghuni, hidup dalam, tinggal.\n
ajjhāsaya: m.  niat, keinginan, dambaan, angan-angan, tekad, watak, pembawaan, kecenderungan, kecondongan.\n
ajjhupagacchati: mendatangi, tiba pada, memperoleh, menyetujui, menerima; rela berkeliling.\n
ajjhupagata: (pp dari **ajjhupagacchati**)  telah datang pada, memperoleh, mencapai.\n
ajjhupekkhati: melihat, meyaksikan, mengamati, memandang dengan penuh perhatian, mengawasi, menjaga; mengabaikan, tidak peduli, acuh tak acuh.\n
ajjhesanā: f.  permohonan, permintaan, hal mengundang, mempersilakan.\n
ajjhokāsa: m.  udara terbuka, ruang terbuka.\n
ajjhogāhati  (ajjhogāheti):  terjun ke dalam, memasuki, masuk ke dalam.\n
añjali: m. perentangan, penangkupan kedua tapak tangan di depan dada sebagai tanda penghormatan; _añjaliṁ paṇāmeti_ memberi hormat dengan merangkapkan tangan.\n
añña: a.  yang lain, lain;**aññamaññaṁ**saling, satu sama lain; **aññena aññaṁ**menjawab dengan jawaban lain (lain pertanyaan lain jawaban); _yāyaññaṁ_  yang lain.\n
aññatara: a.  suatu, tertentu. (→ eka)
aññattha: ☞  **aññatra**
aññatra: adv.  di tempat lain, di suatu tempat lain; lain; tetapi, selain, kecuali; _kiṁ aññatra_ siapa lagi selain, di luar; **nāññatra** walaupun … tidak …, terlepas dari apakah … atau tidak.\n
aññathatta: nt.  perubahan, pengubahan, perpindahan, pemindahan; perbedaan; kesalahan, kekeliruan, pengandaian; plin-plan, perubahan pikiran, kebimbangan, keragu-raguan, terombang-ambing.\n
aññathā: adv.  dengan cara yang berbeda, sebaliknya, secara lain.\n
aññā: f.  pengetahuan, pemahaman, pengertian, pengetahuan sempurna, pengetahuan tertinggi;  _aññāya saṇṭhaheyya_ dapat meraih pengetahuan tertinggi.\n
aṭṭa: 1. m. menara pengintai; menara; podium, panggung; 2. m. perkara hukum, kasus, sebab atau alasan; 3. a. menderita, tersiksa, dilanda, dianiaya, diganggu, disakiti; **~ssara** m. suara mengerang atau merintih.\n
aṭṭaka: m.  panggung yang dipasang di atas tiang-tiang atau pohon, perancah, tangga-tangga; podium.\n
aṭṭiyati: berada dalam kesulitan atau kecemasan, _cemas_, risau, merasa canggung.\n
aṭṭha: 1. a.  delapan [asta ← Skt. aṣṭa]; 2. = **attha** makna, arti.\n
aṭṭhama: kedelapan, ke-8, VIII.\n
aṭṭhi: 1. tujuan, arti, makna, hakikat; 2.  nt. tulang; biji (buah).\n
aṭṭhika: nt.  tulang; biji (buah).\n
aḍḍha: 1. (= **addha**) setengah; 2. a. kaya, makmur; **~yoga**m. bangunan yang atapnya seperti lengkungan sayap burung garuda, bangunan yang atapnya miring ke satu sisi; **~sāra**a.  bernilai setengah.\n
aṇḍa: nt.  telur; buah zakar/pelir; **~kosa**m.  cangkang telur; **~ūpaka** nt.  kumparan, bantalan.\n
ataccha: nt.  tidak benar, salah.\n
atikaḍḍhati: menghela kuat, sulit, sukar, bersusah payah; menyinggung perasaan, melukai.\n
atikkanta: (pp dari **atikkamati**)  a. melewati, melebihi, melampaui, mengatasi; **~mānusaka**melebihi manusia biasa.\n
atikkamati: melewati, melampaui, mengatasi, melebihi, mengalahkan.\n
aticārin: a.  berbuat serong, berzina, menyeleweng, berselingkuh.\n
atithi: m.  tamu, orang asing, pendatang.\n
atipāta: m.  penyerangan, pembunuhan, penghancuran, pembinasaan.\n
atibhuñjati: makan berlebihan, makan terlalu banyak.\n
atimaññati: memandang rendah, meremehkan, mengabaikan.\n
atimāna: m.  keangkuhan, kecongkakan, tinggi hati.\n
atireka: a.  berlebihan, kebanyakan, melebihi, ekstra;  **~cīvara**jubah ekstra;  **~pāda**lebih dari satu pāda.\n
ativatta:  (pp dari **ativattati**) terlewat, terlampau, lampau, teratasi, takluk.\n
ativattati: melewati, melampaui, mengarungi, menguasai, menaklukkan.\n
ativiya: sangat, amat.\n
atiharati: membawa, memindahkan, menarik menuju; kaus. **atiharāpeti** membuat membawa menuju, merenggut, membawa masuk, memperoleh, memanen, mengumpulkan, mengambil alih.\n
atīta: a. yang lampau, yang telah lewat; nt. masa lampau; **atīte** di zaman lampau.\n
atta: 1. (pp dari **ādadāti**) yang telah diambil atau digenggam, yang telah diterima atau dianggap; **~daṇḍa** dia yang memegang sebuah tongkat di tangan, orang yang ganas; **~ñjaha** meninggalkan apa yang telah diterima (dianggap) atau diasumsikan; Mahāniddesa menjelaskan _attaṁ  pahāya_ sebagai _attadiṭṭhiṁ pahāya_ yakni melepaskan 62 pandangan salah; 2. (pp dari **añjati**).\n
attan (atta)  : m.  jiwa, diri yang hakiki; sendiri, diri sendiri (_attānaṁ sukheti pīṇeti_  ia membuat dirinya bahagia dan puas); **~ūpanāyika**a.  berkenaan dengan diri sendiri, ada pada dirinya, dengan merujuk ke dirinya; **~kilamatha** m. penyiksaan diri.\n
attabhāva: m.  sifat pribadi; pribadi, individu, kepribadian, orang, oknum, makhluk hidup, wujud, penampakan, sifat, tabiat, kualitas batin; sosok individu; kehidupan, kelahiran kembali; **~paṭilābha** m. penjelmaan menjadi sesosok makhluk.\n
attamana: a. gembira, suka cita, riang.\n
attha: 1. m.  kesejahteraan, keuntungan (_attadattho_  kepentingan diri sendiri), berkah; harta kekayaan, kebutuhan, keperluan; kebajikan, kebaikan, kegunaan, manfaat; keinginan, tujuan, objek, akibat, arti, makna, alasan; untuk; hal, perkara, kejadian, kasus; **atthena **oleh karena; **~uppatti **makna situasional; **~kara** a. bermanfaat, berfaedah, berguna; **~cariyā** f. perbuatan atau tindakan yang bermanfaat, yang mendatangkan kemaslahatan atau kesejahteraan; **~vasa**kemasukakalan, alasan, akibat, sebab; **~saṁhita** a. bermanfaat, membawa manfaat, menguntungkan, mendatangkan kemaslahatan; 2. nt. rumah, kediaman, peristirahatan. [harta/ arti/arta ← Skt. artha]
atthaṁgama: m.  hal musnah, lenyap, enyah, hilang, terbenam.\n
attharaṇa: nt.  penutup, seprai, kain alas, pengalas, pelapik, permadani, babut.\n
atthi: ada.\n
atthika: a.  bermanfaat, baik, pantas, cocok; yang dikehendaki, yang diperlukan, yang diharapkan, yang dicari, yang dimaksudkan.\n
atra: adv.  di sini.\n
atha: dan, dan juga, kemudian, lantas, lalu, maka; **atha kho**_waktu itu_, lalu, lantas, sekarang, sementara itu, sebaliknya, di satu pihak, tetapi, namun, arkian  (maka) (sesudah itu, kemudian dari itu) adapun, akan hal, mengenai, dalam pada itu, alkisah (maka), sebermula, syahdan (maka), kalakian, hatta (maka);** atha kho pana**namun; **atha kho so** lantas ia benar-benar; **atha ca pana** di pihak lain, sebaliknya;  **atha vā** atau [atau ← Skt. atha vā]
addha: 1. (= **aḍḍha**)  setengah; 2.  (= **adda**) kotor, basah, melekat pada, kecanduan terhadap.\n
addhagata: a.  berusia lanjut. (_addhānaṁ gate dve tayo rājaparivatte atīte, maggapaṭipanne brāhmaṇānaṁ vatacariyādimariyādaṁ avītikkamma_)
addhan: m.  jalan, perjalanan; lintasan; jangka waktu (_dīghaṁ addhānaṁ_  jangka waktu sangat lama), periode, masa (_tayo addhā_ tiga masa).\n
addhā: adv. tentu saja, pasti, sungguh; m. jalan; waktu.\n
addhāna: nt.  jalan, perjalanan, lintasan; jangka waktu; masa; **~magga** m. jalan raya, jalan lintasan, perjalanan jauh.\n
adhakkhaka: m.  di bawah tulang leher.\n
adhi: (menunjukkan arah gerakan ke suatu sasaran) ke, kepada, terhadap, menuju, pada, ke atas; (menunjukkan lokasi) di atas, di, pada, sini (**adhi** + **atta** = **ajjhatta** pada diri sini)
adhikaraṇa: nt.  pendampingan, penjagaan, pengawasan, pengelolaaan, administrasi; hubungan, rujukan, alasan, sebab, akibat; _kasus_, _perkara_, masalah, pokok soal, topik pembahasan, perselisihan.\n
adhikāra: m. pelayanan, pengawasan, pengelolaan, bantuan; niat, harapan.\n
adhigacchati: mencapai, meraih, menemukan, menyelami, memahami, mewujudkan.\n
adhigaṇhāti: melampaui, melebihi, melewati.\n
adhigata: a.  dikuasai, dicapai, dimiliki, ditemukan, diwujudkan.\n
adhigama: m.  pencapaian, perolehan, pengetahuan, informasi, hasil belajar.\n
adhiṭṭhāti (adhiṭṭhahati): berdiri (di atas), bersikukuh; memusatkan perhatian pada, mengarahkan pikiran seseorang pada, berketetapan hati, bertekad, mengharapkan, melakukan, menjalankan, mempraktikkan, memelihara, menyelenggarkan, menjaga, berkemauan, menentukan, memastikan, menetapkan.\n
adhiṭṭhāna: nt.  pijakan yang kokoh; tekad, ketetapan hati, kekukuhan pada; a. yang sudah ditetapkan atau ditekadkan.\n
adhiṭṭhita: (pp dari **adhiṭṭhāti**)  berdiri di atas, bersikukuh atas; dipelihara atau dijaga, dilakukan, dikerjakan, diurus; bertekad.\n
adhipati: m.  1. penguasa, adipati, tuan; 2. berkuasa atas, berdaulat atas, dikuasai oleh; **attādhipati**memiliki harga diri; **lokādhipati** menghargai orang lain. [adipati ← Skt. adhipati]
adhippāya: m.  niat, maksud, keinginan, tujuan, hasrat, kehendak; makna, arti, titik tolak, kesimpulan; **adhippāyena**dengan cara, seperti.\n
adhippeta: a.  yang diinginkan atau dikehendaki, yang berkenan di hati; yang dimaksudkan, yang dipahami, yang bermakna.\n
adhibhāsati: berkata kepada, bertutur kepada, berucap kepada.\n
adhimāna: m.  penilaian berlebihan (terhadap diri sendiri), keangkuhan.\n
adhimuccati: tertarik pada, terpikat pada, condong pada, hanyut dalam; memutuskan, bertekad untuk, menjadi jelas (paham) atas; berkeyakinan, tak goyah terhadap; merasuki; kaus. **adhimoceti**condong pada, mengarahkan.\n
adhimutta:  (pp dari **adhimuccati**) mendambakan, menghasratkan, mengerahkan diri pada, tertarik pada, condong pada, cenderung, menjadi terpikat.\n
adhivacana: nt.  istilah, sebutan, atribut, kiasan, metafora, ungkapan metafora; (**urena gacchati ti urago sappass’etaṁ adhivacanaṁ**).\n
adhivattha: (pp dari **adhivasati**)  mendiami, tinggal, bersemayam.\n
adhivāsana: nt. persetujuan, izin atau perkenan, kesabaran.\n
adhivāseti: menunggui, bersabar menerima, menyetujui, berkenan, memperturutkan.\n
adhisayita: (pp dari **adhiseti**) diduduki.\n
adhisīla: nt.  moralitas yang lebih tinggi, sila nan luhur.\n
adhiseti: berbaring di atas, duduk di atas, hidup dalam, mengikuti.\n
adho: adv.  di bawah; **adhakkhaka**m.  di bawah tulang leher.\n
anattā: nt.  tiada aku, bukan diri, tiada suatu inti atau substansi yang kekal.\n
anatthika: a.  yang tidak peduli terhadap, yang tidak puas dengan, yang tidak baik; tidak bermaksud apa-apa.\n
anabhāva: m. lenyap sama sekali.\n
anavaya: a.  tidak kekurangan, penuh dengan, sempurna dalam.\n
anassāsaka: a.  tidak dapat bernapas, sesak napas.\n
anāgata: a.  belum datang, kelak, di kemudian hari, di masa mendatang, belum terjadi, belum sampai, belum berhasil.\n
anāgāmin: a. m.  yang takkan kembali lagi, yang telah mencapai tingkat kesucian ketiga.\n
anācāra: m.  perilaku buruk, kebiasaan buruk.\n
anātha: a.  tiada pelindung (perlindungan), miskin.\n
anārambha: m.  yang tidak merepotkan.\n
anicca: a. nt.  tak langgeng, tak kekal, sementara.\n
aniṭṭhita: a.  belum selesai, belum lengkap, belum habis, belum kelar.\n
animitta: n.  tanpa tanda, tanpa atribut, tak tercemar, tak terpengaruh, tidak berkondisi.\n
anissita: a. tidak ditopang oleh, tidak menempel pada, bebas, terbebas.\n
anītika: a.  bebas dari cedera, bebas dari bahaya, sehat, aman.\n
anukantati: memopong, menyobek, mengiris.\n
anukampā: f.  kasihan, sayang.\n
anugacchati: mengikuti, membuntuti, memasuki, termasuk.\n
anugata: (pp dari **anugacchati**) diikuti, disertai, tiba pada, mengikuti; termasuk dalam, terpaut dengan; menjadi korban dari, menderita.\n
anuggaha: a.  tidak mengambil;  m.  pengambilan, belas kasih, cinta kasih, bantuan, manfaat, kemaslahatan.\n
anucinteti: memikirkan, merenungkan, mempertimbangkan.\n
anucchavika: a.  “sesuai dengan kulit seseorang”, cocok, pantas, sesuai, patut, layak, serasi, seiring, selaras, sepadan.\n
anujānāti: mengizinkan, memperkenankan, membolehkan, menasihati, menentukan, memformulasikan (merumuskan); **anuññeyya** yang dibolehkan.\n
anuññāta: (pp dari **anujānāti**) diizinkan, diperbolehkan, disetujui, didukung, diperkenankan, ditahbiskan, dinobatkan.\n
anuttara: a.  tiada yang melebihinya, tiada banding, tiada taranya.\n
anuddayā (anudayā):  rasa belas, rasa kasihan, rasa iba, sayang.\n
anuddhaṁseti: menggerogoti, mengganggu, menjerumuskan, melanda, merusak, menghina, mengutuk, menghujat.\n
anunaya: “menuntun menyusuri”, keramahtamahan, kesopanan, kasih sayang.\n
anuneti: membuat bersahabat, mengambil hati, memperlakukan dengan baik.\n
anupagacchati: pergi atau kembali ke.\n
anupatati: mengikuti, menyusuli, menguntit; menyerang, menyerbu.\n
anupatta: (pp dari **anupāpuṇāti**)  telah mencapai, meraih, menggapai, mendapatkan.\n
anupadesa: m.  pedesaan.\n
anuparigacchati: (berjalan) mengitari, berkeliling, berputar-putar, mengelilingi.\n
anupassati: melihat, menilik; merenungkan, mengamati, mencermati.\n
anupassin: a.  melihat, memandang, mengamati, menyadari.\n
anupādā: adv.  tidak lagi mengambil (bahan bakar untuk mempertahankan api kelahiran kembali), tidak melekat pada kerinduan terhadap dunia ini.\n
anupādāya: adv.  tidak melekat pada, bebas, tidak berkondisi.\n
anupāpuṇāti: mencapai, tiba pada, sampai.\n
anupubba: a.  secara berturut-turut, secara beruntun, secara bertahap, secara teratur, secara berangsur-angsur; segera;  **anupubbena** segera, akhirnya, belakangan, secara bertahap.\n
anupekkhati: merenungkan.\n
anuppatta (anupatta): (pp dari **anupāpuṇāti**) dicapai, diterima, tiba, sampai.\n
anubandhati: mengikuti, menguntit, mengejar, menyusuli.\n
anubuddha: (pp dari **anubodhati**) telah mengalami pencerahan, sadar, mengenali, melihat, mengetahui; **buddhānubuddha** mengalami pencerahan oleh (bimbingan dari) ia yang telah mengalami pencerahan.\n
anubhavati: datang ke; mengalami, menderita; melakukan, mengambil bagian dalam; makan.\n
anubhavana: nt.  hal mengalami, menderita, sensasi atau kemampuan tubuh untuk merasakan; menghayati.\n
anubhāva: m.  “pengalaman, hal yang bersamaan”, mengalami sensasi dari, milik dari, sesuai dengan; kekuatan, keagungan, kegemilangan, daya, kehebatan, keperkasaan.\n
anubhoti (anubhavati): lantas menjadi, sampai pada, menjalani, ikut serta atau mengambil bagian dalam, mengalami, makan, mengalami.\n
anumati: f.  persetujuan, izin, perkenan.\n
anummatta: a. tidak gila, waras.\n
anuyāyin: a.  mengikuti.\n
anuyuñjati: mempraktikkan, melakukan, melibatkan diri, mengurus, menindaklanjuti; menanyakan, menyidik, menginterogasi, menegus; kaus. **anuyojeti**mewejang, menasihati.\n
anuyutta: (pp dari **anuyuñjati**)  mengupayakan, mengamalkan; mengikuti, mengurusi;  m.  pelayan, hamba, pengiring.\n
anuyoga: m.  pengamalan, pelaksanaan, praktik; _anuyogaṁ anuyutta_  pengamalan;  a.  melakukan, melaksanakan, mengamalkan, menuruti.\n
anurakkhaṇa: nt. hal melindungi, menjaga, melestarikan, mengayomi (?).\n
anulepa: m. pengolesan, pelumuran.\n
anulomika: a.  cocok, pantas, sesuai, serasi; dengan urutan yang tepat, disesuaikan terhadap.\n
anuvattaka: a.  yang melanjutkan (suatu kekuasaan), ahli waris, mengikuti, berpihak pada.\n
anuvāda: m.  celaan, kecaman, teguran, tuduhan, dakwaan.\n
anuvicarati: berkeliling meninjau, berkelana.\n
anusaññāti: pergi ke, mengunjungi, menginspeksi, meninjau, mengawasi, memeriksa.\n
anusaya: m.  kecondongan, kecenderungan, sifat laten, tendensi, obsesi, nafsu laten.\n
anusāra: m.  hal mengikuti atau bersesuaian dengan; **anusārena** bersesuaian dengan, akibat dari.\n
anusārin: a.  berusaha sejalan dengan, mengikuti, bertindak sesuai dengan.\n
anusārī: a.  berjuang, berupaya; bertindak sesuai dengan.\n
anusāsati: menasihati, memberi wejangan; memerintah, mengurusi.\n
anusāsana: nt.  nasihat, wejangan, petuah.\n
anusāsanī: f.  wejangan, nasihat, anjuran, instruksi, ajaran, perintah.\n
anussati: f.  ingatan, hal mengingat atau mengenang, perenungan, hal menyadari, hal mengarahkan pikiran pada.\n
anussarati: mengingat-ingat, mengenang, merenungkan, menyadari, mencamkan.\n
anussāveti: memperdengarkan, mengumandangkan, menyiarkan, mengabarkan, berseru.\n
anussuta: 1. a. bebas dari nafsu, tanpa nafsu; 2. terdengar.\n
aneka: a.  banyak, berbagai, jamak, aneka, tak terbilang; **~pariyāyena** dengan berbagai cara, dengan beragam cara;  **~vihita**aneka macam, beragam. [aneka ← Skt. aneka]
anokāsa: m.  tanpa kesempatan; **~kata** tanpa mendapatkan izin.\n
anodissa: adv.  tanpa sasaran, tanpa batas.\n
anodissaka: a.  tanpa batas, tanpa kecuali, umum, universal.\n
anta: 1. m. ujung, penghujung, tamat, akhir, penghabisan, tujuan, sasaran; batas, perbatasan, sempadan, tepi, pinggir, susur; sisi, hadapan, sisi atau pihak lawan, ekstrem, bagian, pihak; 2. a. berujung, ujung, akhir, ekstrem, terakhir, ter, terburuk; 3. nt. usus.\n
antamaso: adv.  bahkan, sekalipun, walaupun.\n
antara: a.  di dalam, di antara, dalam, ada di dalamnya, mengandung (**āmisantara** ketamakan ada di dalamnya, tamak); berjarak; nt. bagian dalam, ruang antara, pertengahan, jeda, rintangan (yang ada di antara), jangka waktu, waktu (**etasmiṁ antare** pada waktu itu), kesempatan, waktu antara, sela waktu, antara, selang waktu (**buddhantaraṁ** selang waktu antara dua Buddha); perbedaan; _antaraṁ karoti_ menjauhi, menjaga jarak dengan, menyingkirkan, menghancurkan; memusnahkan; **antarantare** tepat di tengah-tengah, tepat di dalam; **antarantarā** dari waktu ke waktu, ada kalanya, berturut-turut; **antarā** (abl.) adv. di antara. [antara ← Skt. antara]
antaradhāna: nt.  hal lenyap˴ hilang˴ musnah.\n
antaradhāpeti: (kaus. dari **antaradhāyati**) melenyapkan, menghancurkan.\n
antaradhāyati: lenyap.\n
antarabhogika: m.  seseorang yang memiliki daya pengaruh di bawah kekuasaan raja atau kerajaan; hulubalang.\n
antaravāsaka: m.  jubah bawah (busana bhikkhu).\n
antarahita: (pp dari **antaradhāyati**)  lenyap, enyah; benda pengantara, pelapik; _anantara-hitāya bhūmiyā_ di atas tanah polos tanpa lapik atau alas.\n
antarāyika: a.  menjadi rintangan atau hambatan.\n
antarika: a.  tengah, berikut, selanjutnya; jauh, di antara, di dalam; anantarika  tanpa sela, langsung, segera.\n
antarikā: f.  yang terletak di antara atau dekat, bagian dalam, lingkungan, daerah di seputar, wilayah; sela, celah.\n
antima: a. terakhir, terbuntut.\n
ante: dekat, di dalam.\n
antevāsika: m.  seseorang yang berdiam atau menginap di dalam; seseorang yang hidup bersama gurunya; siswa (dari _ācariya_), murid cantrik.\n
anto: dalam, di dalam, bagian dalam, ke dalam; **~mano** murung, sayu, sedih, muram.\n
andu: m.  rantai, belenggu.\n
andha: a.  buta, gelap; kabur, tumpul; **~kāra**m.  kegelapan, kebingungan, kebutaan, kedunguan.\n
anna: nt. makanan.\n
anvaddhamāsaṁ: adv. setiap setengah bulan.\n
anvaya: m.  kesesuaian, kecocokan; proses; a. mengikuti, dengan jalur yang sama, bersesuaian dengan; setelah (mengikuti).\n
anvāya: setelah mengikuti, mengalami, mencapai; akibat dari, karena, setelah.\n
apakaroti: mencampakkan, menghilangkan, melukai, menyerang, mengabaikan, menggempur.\n
apagata: (pp dari **apagacchati**) pergi, pergi meninggalkan, pergi menjauhi, pindah, meninggal dunia; tanpa, bebas dari, lenyap.\n
apagabbha: a.  takkan muncul lagi dalam kandungan/rahim; takkan dikandung lagi, takkan dilahirkan kembali.\n
apacaya: m.  penanggalan, pengikisan, peluluhan, penciutan.\n
apacāyati: menghormati, respek terhadap, memuja-muja.\n
apacita: (pp dari **apacāyati** atau **apacināti**) dihormati, disembah.\n
apadisati: memanggil menyaksikan, merujuk ke, mengutip.\n
apaneti: membawa pergi, mengambil pergi, memindahkan (=**harati**).\n
apara: a.  yang lain, yang berikut; barat; _aparaṁ divasaṁ_  di suatu hari setelah ini; _apare divare_  pada hari lainnya; _apare tayo sahāyā_  tiga (se)kawan; _aparaṁ_  adv. selanjutnya, di samping itu, juga; _athāparaṁ_  selanjutnya, lagi pula; **aparena**di masa mendatang; **aparāparaṁ**ke sana sini, berulang-ulang, berkali-kali.\n
aparajjhati: bersalah atau melakukan kesalahan kepada.\n
aparaṇṇa: nt.  serealia lain, serealia matang; kacang-kacangan, palawija (?).\n
aparaṇha: m.  sore hari.\n
aparaddha:  (pp dari **aparajjhati**) meleset, salah jalan, nyasar, bersalah, gagal.\n
aparādha: m. dosa, kesalahan.\n
aparādhika: a. berdosa, bersalah, kriminal.\n
apalokita: (pp dari **apaloketi**)  minta izin, berkonsultasi, minta pamit; nt. izin, persetujuan; sebutan untuk nibbana; cara berpandang (_nāgāpalokitaṁ apalokesi_ memandang dengan cara berpandang gajah).\n
apaloketi: memandang kemuka, berhati-hati, menjaga, memandang ke, mendapat izin dari, meminta izin, minta diri, minta pamit, berpamitan, memberitahu, memperingatkan.\n
apasādeti: menolak, menyangkal; merendahkan, menistakan, meremehkan, menyanggah.\n
apassaya: m.  penopang, penyangga; pembaringan, rajang, bantal, tilam, kasur.\n
apassāya: bersandar.\n
apassena: nt.  sandaran, dudukan, penopang, kalang; **~phalaka**papan penopang (kepala).\n
apaharati: mengambil pergi, memindahkan, menyingkirkan, merampas.\n
apāpuraṇa (avāpuraṇa): nt.  kunci (pintu).\n
apāpurati (apāpuṇati): membuka (pintu).\n
apāya: pergi, hilang, musnah, bocor, kuras, tergelincir, merosot; **~mukha** nt. jalan menuju kehancuran atau pengurasan atau kemerosotan.; m. alam rendah.\n
api: juga, lagi, pula, dan juga; namun, bahkan, mungkin, walaupun; mungkin, bisa jadi; **app eva nāma**tentu saja, ya, saya pikir, saya kira, mungkin, bisa jadi, barangkali; **api ca**dan juga, lagi pula, selanjutnya, lebih lanjut, tetapi; **api ca kho** namun, melainkan; **apissu**sampai-sampai.\n
apuñña: nt.  kemudaratan.\n
apekkha (=apekkhā): a.  menantikan, mengharapkan, mencari, menginginkan, berniat.\n
apekkhati: mengharapkan, mengidamkan, menantikan, berhasyat akan.\n
apekkhavant: a.  penuh hasrat, penuh keinginan, mendambakan, berhasrat.\n
appa: a.  sedikit, kecil, secuil, sekelumit, sepele; pendek; nt. sedikit, secuil, sepele; **~āyuka** berusia pendek.\n
appaka: a.  sedikit, kecil, sepele; _appakena_  dengan mudah.\n
appaṭibhāṇa: a. tak dapat menjawab atau membantah, tak berucap sepatah kata pun; menjadi bingung atau galau, tidak mantap (hati), kecut hati.\n
appaṭivekkhiya: (ger.) tanpa mengamati atau memperhatikan.\n
appaṭisandhika: m.  yang tak dapat disambung atau disatukan kembali, yang tak dapat dikembalikan ke keadaan semula, yang takkan terlahir kembali.\n
appaṇihita: a.  tanpa tujuan, tidak condong pada apa pun, bebas dari (objek) keinginan, tanpa pamrih.\n
appatīta: a.  tidak puas, tidak senang, kecewa, kesal, tidak suka.\n
appamatta: a.  tidak lengah, awas, waspada, sadar, penuh perhatian; secuil, sepele, sedikit, sekelumit.\n
appamattaka: a. nt.  sedikit, sekelumit, secuil.\n
appamāda: m.  ketidaklengahan, kewaspadaan, hal penuh sadar, tak leka, keseriusan.\n
appiya: a. yang tidak disenangi˴ disukai˴ berkenan di hati.\n
appoṭheti (apphoṭeti) :  bertepuk tangan, memetik jari.\n
abbuda: m.  janin 1-2 bulan setelah pembuahan; tahap kedua dari lima tahap perkembangan janin (_kalala, abbuda, pesi, ghana, pasākha_); tumor, bisul, seriawan; suatu bilangan yang sangat besar; neraka.\n
abbohārika: a.  tidak dalam cakupan hukum atau peraturan, dapat diabaikan, merupakan pengecualian.\n
abbhañjati: meminyaki.\n
abbhantara: a.  di dalam, di antara; **abbhantaraṁ**nt.  bagian dalam, interior, interval; **abbhantarena**dalam waktu bersamaan, di antara.\n
abbhantarima: a.  bagian dalam, internal.\n
abbhākuṭika: a.  tidak mengernyitkan alis, peramah, tidak sombong.\n
abbhāghāta: m.  pelaksanaan hukuman mati.\n
abbhuggacchati: mencuat, menyebar, muncul.\n
abbhuta:   1. a. nt.  menakutkan, mencengangkan, aneh, luar biasa, dahsyat, membingungkan atau menimbulkan teka teki, menakjubkan, ajaib atau supernormal, menawan hati; ~dhamma  fenomena misterius, sesuatu yang menawan hati, ajaib; salah satu ragam kitab suci (▶ navaṅgabuddhasāsana); 2. nt. taruhan; _abbhutaṁ karoti (sahassena)_ bertaruh (1000 kepeng).\n
abbheti: merehabilitasi (seorang bhikkhu yang diskors atas pelanggarannya terhadap winaya).\n
abyākata: a.  tidak  terjawab, tidak terputuskan, tidak terungkapkan; kamma yang tak dapat dikatakan kusala atau akusala; dalam Dhs.A. (p.261) dikatakan ada 4 hal yang dikategorikan sebagai _abyākata_ yakni _vipāka_, _kiriya_, _rūpa_, dan _nibbāna_.\n
abhabba: a.  tak mungkin, mustahil, takkan, tak dapat.\n
abhaya: a.  bebas dari ketakutan atau bahaya, tak gentar, aman, bebas dari ancaman.\n
abhāva:   m.  tidak ada, lenyap, sirna.\n
abhikkanta: (pp dari **abhikkamati**) berjalan maju, meluncur pergi, melesat maju, memudar; bagus, hebat, unggul; menyenangkan, asyik, yahud, hebat, luar biasa; elok, indah sekali _(abhikkanta saddo khayasundarābhirūpa abbhanumodanesu dissati)._
abhikkamati: berjalan maju, menghampiri.\n
abhijāna: m. nt.  hal mengetahui, menguasai, ingat, menyelami; pengetahuan mendalam.\n
abhijānāti: mengetahui sepenuhnya, mengetahui dengan mengalami, menyelami, mengenal, _mengalami langsung_.\n
abhijjamāna: a.  yang tak tercerai-berai atau terbagi.\n
abhijjhā: f.  kerinduan, dambaan, keserakahan, ketamakan, nafsu loba, tergiur akan.\n
abhiññā: (pp dari **abhijānāti**) setelah menyelami, setelah memahami betul, setelah diselami dengan pengetahuan istimewa, setelah menyadari;  f.  pengetahuan istimewa, pengetahuan hasil penyelaman, pengetahuan hasil penembusan batin, pengetahuan langsung, kekuatan supranatural, kemampuan batin luar biasa, _pengetahuan batin luar biasa_.\n
abhitāpa: a.  panas sekali;  m. panas tinggi, memijar; **sīsābhitāpa** kelengar matahari, sakit kepala.\n
abhidosika: semalam, malam sebelumnya.\n
abhinandati: bersukacita, bergembira.\n
abhinandin: a. senang dengan, suka terhadap, gemar akan.\n
abhiniggaṇhanā: f.  hal menahan, mencengkam.\n
abhiniggaṇhāti: menahan, mencengkam, mengendalikan, mencegah, melarang, menghalangi.\n
abhininnāmeti: mengarahkan kepada, memalingkan kepada.\n
abhinippīḷanā: f.  hal menekan, memencet, menggencet, memeras, meremas, memegang, mencubit.\n
abhinippīḷeti: memencet, menggencet, memeras, menggilas, menaklukkan.\n
abhinibbatti: f.  hal menjadi, mengada, terlahir, terlahir kembali, menelorkan.\n
abhinibbijjhati: menerobos.\n
abhinibbidhā (abhinibbhidā)  : f.  penerobosan keluar (dari cangkang telor), penetasan.\n
abhinimmināti: menciptakan (dengan kekuatan gaib), menghasilkan, membentuk, membuat.\n
abhiniropana: nt.  mengarahkan perhatian atau pikiran pada.\n
abhinivesa: m.  “tiba di”, mengharapkan, mendalami, menguasai, kecondongan terhadap, kecenderungan, kesetiaan, ketaatan, mengambil kesimpulan, melakukan penafsiran; a. menyukai, menyenangi, condong terhadap.\n
abhinisīdati: duduk dekat, duduk di atas.\n
abhinīta: (pp dari **abhineti**)  dituntun ke, dibawa ke, dibantu oleh.\n
abhipīḷeti: menekan, menggilas; menyiksa.\n
abhippamodati: senang, merasa puas, girang, gembira.\n
abhippasanna: (pp dari **abhippasīdati**)  menemukan kedamaian batin dalam, mempercayai, meyakini, berkeyakinan penuh terhadap, berbakti kepada.\n
abhippasīdati: memiliki keyakinan terhadap, mengagumi
abhibhūta: (pp dari **abhibhavati**)  ditaklukkan, dikalahkan, diatasi, ditundukkan, dikuasai.\n
abhimaṅgala: a.  (sangat) beruntung, mujur, penuh berkah.\n
abhimukha: a.  menghadap, mengarahkan muka pada, menghampiri, berpaling kepada; adv. ke, menuju.\n
abhiyuñjati: menuduh, mendakwa, mengadukan, menuntut, menjadi beban tanggung jawab seseorang.\n
abhirata: (pp dari **abhiramati**) gemar, merasa senang dalam, suka akan, betah.\n
abhirati: f.  kesenangan, kegembiraan dalam (lok.).\n
abhiraddha:  a.  berkenan, puas, marem.\n
abhiramati: bersenang-senang, berhiburan, betah; **yathābhiranta** sekehendak hati, sesuka hati, sebagaimana yang diinginkan.\n
abhirūpa: a.  berwujud sempurna, (sangat) ganteng, cantik, elok, rupawan, jombang.\n
abhirūḷha: (pp dari **abhirūhati**)  dipanjat, didaki, dinaiki.\n
abhirūhati: menaiki, mendaki, memanjat, melanjutkan, memasuki.\n
abhivassati: hujan, mengguyur, mencurah, turun hujan.\n
abhivādana: nt.  penghormatan (dengan membungkuk), memberi salam dengan takzim.\n
abhivādeti: membungkuk, memberi hormat, menyalami, menyambut, hormat terhadap/kepada
abhiviññāpeti: membujuk, mengajak.\n
abhivitarati: menyelami, memperhatikan, mengamati, memahami betul.\n
abhisaṅkhārika: a.  yang termasuk dalam atau dilakukan oleh _saṅkhāra_; terkumpul oleh atau pengumpulan jasa-jasa kebajikan; yang disiapkan secara khusus; istimewa.\n
abhisanda: m.  hal mengalir, meluber, menghasilkan, menelurkan.\n
abhisandahati: meletakkan bersama, mengumpulkan, menggiring, menyiapkan; ger. **abhisandhāya** disebabkan oleh.\n
abhisanna: a.  penuh dengan, kebanjiran, kepenuhan, menyesak.\n
abhisamācārika: a.  yang mengarah ke perilaku yang baik yang paling dasar.\n
abhisameta: (pp dari **abhisameti**)  dicapai atau diwujudkan sepenuhnya, dipahami, dimengerti, dikuasai.\n
abhisameti: mencapai, menggapai, mewujudkan, memperoleh; mengerti, memahami, menguasai.\n
abhisambujjhati: menyadari seutuhnya, menyelami pengetahuan tertinggi, meraih kebijaksanaan tertinggi.\n
abhisambuddha: (pp dari **abhisambujjhati**)  a. terwujud atau diselami secara sempurna;  m. orang yang telah mewujudkan kebijaksaan tertinggi, yang telah sadar penuh, yang telah meraih kebuddhaan, yang telah mewujudkan pencerahan batin.\n
abhiharati: membawakan, mempersembahkan, mengambil(kan); mengutuk, memaki, mencaci.\n
abhihāra: m.  bawaan, persembahan, hadiah.\n
amacca: m.  kawan, sahabat, rekan, penolong, teman karib, rekan penasihat, penasihat karib, rekan sekerja; teman karib Raja, rekan pendamping Raja, rekan kepercayaan Raja, penasihat khusus Raja.\n
amanussa: m.  makhluk bukan manusia, peri, makhluk halus, hantu, yakkha.\n
amutra: adv. di tempat anu, di situ, dalam kelahiran itu.\n
amba: m.  mangga (_Mangifera indica_).\n
ambho: he.\n
amma: mama, mami, bu, mak (panggilan sayang terhadap ibu).\n
ammā: f.  ibu.\n
ayo  (aya): nt. besi.\n
ayoniso: secara tak teratur, secara tak bijaksana, tak patut; **~manasikaroti**tanpa menghiraukan, tidak memperhatikan secara patut atau bijaksana, tidak mengindahkan.\n
ayya: a.  mulia;  m.  tuanku, nyonya, yang mulia, panggilan terhadap seorang bhikkhu atau bhikkhuni; panggilan umat wanita terhadap bhikkhu; **~putta**m. tuan muda.\n
ayyaka: m. kakek.\n
ayyakā (ayyikā): f. nenek.\n
arañña: nt.  hutan.\n
arasarūpa: nt.  sosok tidak bercita-rasa.\n
araha: a.  layak atau patut menerima; cocok, sesuai; bernilai, berharga.\n
arahati: patut, layak, pantas.\n
arahant: a.  arahat (sebelum munculnya Buddhisme, digunakan sebagai sebutan hormat untuk pejabat tinggi. Saat Buddhisme sedang berkembang, diterapkan secara populer terhadap semua petapa. Juga diserap kaum Buddhis untuk seseorang yang telah meraih pencapaian tertinggi nibbana.)
ari: m.  musuh, seteru.\n
ariṭṭha: a. kejam, sial; m. burung gagak; pohon nimba.\n
aritta: nt.  kemudi (kapal);  a. tidak kosong dari; tidak tanpa.\n
ariya: a.  mulia, unggul, berdarah mulia (ningrat); dari suku (ras) Aria; sesuai dengan adat, norma, idaman, yang dijunjung kaum Aria; benar, baik, elegan, sejati, ideal; Ariya;  m. seseorang yang mulia (batinnya), seseorang yang telah meraih pengetahuan tertinggi, orang suci (_ariyānaṁ upavādaka_). [arya ← Skt. ārya]
ariyaka: m.  seseorang yang berasal dari kaum (suku) Ariya; bahasa kaum (suku) Ariya; bahasa Magadha; tutur kata yang pantas.\n
alaṁ: ungguh, betul-betul (_alam antarāyāya_  sungguh merupakan suatu rintangan); pantas, sesuai (_alam eva kātuṁ_  ini pantas untuk dilakukan; _alaṁ hi te gāmaṇi kaṅkhituṁ, alaṁ vicikicchituṁ_); cukup (_alam ettāvatā mahārāja, kataṁ ettāvatā mahārājāti_ cukupkah segitu, Maharaja, bolehkah segitu?) awas, hati-hati.\n
alaṁkata:  (pp dari **alaṁkaroti**) didandani, dihiasi, disiapkan, dipersolek; dibuat cukup, dibubuhi.\n
alaṁkaroti: menghiasi, mendekorasi, mendandani, membubuhi.\n
alaṁkāra: m.  persiapan, hiasan, dekorasi, dandanan.\n
alasa: a. lamban, malas, kendur, lesu.\n
alika: a.  berlawanan, salah, tidak betul; nt. bohong, keliru.\n
allīyati: melekat pada, menempel pada, mencantol pada, mematuhi.\n
avakāsa: (**okāsa**) m.  penampakan; kesempatan, kemungkinan; **anavakāsa**m.  tidak mungkin, mustahil.\n
avaca: a.  rendah.\n
avacara: a.  hidup dalam atau dengan, bergerak dalam, berkecimpung dalam, akrab dengan, mahir dalam;  m. lingkup (aktivitas), _ranah_, dunia, alam.\n
avajja: a.  rendah, inferior, tercela, buruk; **anavajja** (lawan dari **sāvajja**) tiada cela, tiada cacat.\n
avaṭṭhita: a.  berdiri, diduduki, ditimpa, kokoh, dipatok, bersikukuh, abadi.\n
avaṇṇa: m.  hal mencela, menyalahkan, mengutuk.\n
avalitta: a.  berturap atau berlepa luar.\n
avasarati: meluncur, pergi ke, akhirnya tiba di.\n
avasiṭṭha: (pp dari **avasissati**) yang tersisa, tertinggal.\n
avasesa: m.  sisa; **anavasesa**a.  tanpa sisa sedikit pun; sepenuhnya, seutuhnya.\n
avassakaṁ: adv.  tak terhindarkan, perlu, mau tak mau.\n
avaharaṇa: m.  hal membawa pergi, mencaplok, menyhingkirkan, mencuri.\n
avaharati (oharati): mencuri, menyelewengkan, mencolong.\n
avahāraka: m.  pencolong.\n
avikampana: nt.  keikhlasan, kerelaan, ketaktergoyahan.\n
avijjā: f.  ketidaktahuan.\n
aviññū: a.  bodoh, tidak tahu.\n
avidūra: a.  tak jauh, dekat.\n
avinipāta: m.  takkan terperosok  ke dalam alam celaka.\n
avirodha: m.  tanpa rintangan, tanpa halangan; santun, lembut.\n
avivāda: m.  tanpa pertentangan, tanpa percekcokan, akur, rukun.\n
avihiṁsa (avihesa): f.  tiada kekejaman, belas kasih, manusiawi, cinta kasih.\n
avecca: 1. adv.  pasti, absolut, tandas, niscaya, mantap, sempurna; 2. sudah tahu (paham).\n
avera: a.  tidak bermusuhan, damai, lembut, bersahabat.\n
avyāvaṭa: a.  tidak sibuk, cuek, tidak peduli.\n
asaññata: a.  tak terkendali, tanpa pengendalian diri.\n
asaddhamma: m.  kondisi (keadaan) jaht, berdosa, hubungan seksual.\n
asambhinna: a.  tak dicampur, tak dipalsu; bening, jernih, jelas (tentang suara); sejenis salap (urap).\n
asammosa: m. ketiadaan kebingungan atau kebuyaran.\n
asallīna: a.  aktif, tegak, tak tergoyahkan.\n
asi: m.  pedang, pisau besar, golok, _parang_.\n
asita: 1. a. yang telah dimakan, makan; nt. makanan, yang dimakan atau disantap; 2. a. tidak melekat, bebas; 3. a. hitam kebiru-biruan; hitam.\n
asuka (amuka): pron. a.  ini, itu, anu, suatu.\n
asuci: a.  tidak bersih, tidak murni, najis; air mani, asuci.\n
asubha: a.  kotor, najis, buruk, jelek, keji, menjijikkan; nt. hal menjijikkan, memuakkan, tak menyenangkan; **~kathā**wejangan perihal kenajisan, khotbah perihal kotor menjijikkan.\n
asura: m.  bukan dewa, asura. (Sejenis makhluk halus yang senantiasa berseteru dengan para dewa. Acapkali disebutkan bersama _garuḷa_ atau _supaṇṇa_, _gandhabba_, _nāga_, dan _yakkha_.)
asūra: a.  pengecut;  lamban malas.\n
asekha (asekkha): a. m.  tak perlu dilatih lagi, sudah sempurna, tak perlu berlatih lagi; Arahat.\n
asecanaka: a.  tak dicampur, tak disubal (dicampuri dengan barang yang kurang baik mutunya supaya kelihatan banyak, bertambah berat, dsb), tak dikotori atau dibumbui (dengan bahan lain), wantah, sempurna, murni.\n
asmimāna: m.  keangkuhan keakuan.\n
assa: 1. bahu; **~puṭa**tas/kantung yang disandang di pundak; 2. sudut, titik; **caturassa**segi empat; 3. kuda; [aswa ← Skt. aṡva] 4. gen. dat. sg. dari **ayaṁ** (ini, nya); 5. sg. Pot. ketiga dari **asmi** (**atthi**) kalau saja, sekiranya, semoga. (**pissa**dia punya juga ….; **tayassa**tiga buah milik dia)
assattha: 1. m. pohon Bodhi, _Ficus religiosa_; 2. (pp dari **assasati**) membesarkan hati, menghibur.\n
assama: m.  pertapaan, tempat bertapa. [asrama ← Skt. āṡrama]
assasati: bernapas, menarik napas, bernapas bebas, bernapas dengan tenang, bernapas lega, merasa nyaman, menjadi lega; masuk melalui napas, memesonakan, merasuk, memikat, menawan hati.\n
assāda: m.  rasa, manis, nikmat, puas.\n
assāsaka: a.  bernapas; m. nt. yang memberi kenyamanan dan kelegaan; kepercayaan, (peng)harapan.\n
ahaṅkāra: m.  keakuan.\n
ahi: m.  ular.\n
ahirika (ahirīka): a.  tak tahu malu, tebal muka, tak cermat.\n
aho: (kata seru yang mengungkapkan keterkejutan, kekaguman, keheranan, kekagetan), aha, wah, oh, alamak; **aho vata** oh kalau saja, oh alangkah bagusnya.\n
ākaṅkhati: menginginkan, menghendaki, mendambakan, berpikir, berniat, merencanakan, mengangankan.\n
ākaḍḍhati: menyeret, menarik, menghela.\n
ākaḍḍhana: nt.  hal menyeret, menarik keluar, terbias.\n
ākāra: m.  cara, keadaan, kondisi; sifat, karakter, kualitas; ciri, tanda, corak, penampakan, wujud; alasan, dasar, dalih.\n
ākāsa: m.  udara, langit, udara terbuka, angkasa, tawang, awang-awang. [angkasa ← Skt. ākāṡa]
ākiṇṇa: (pp dari **ākirati**)  ditaburi, disesaki, dipenuhi, dikelilingi, dipadati (**ākiṇṇaloma** berbulu lebat atau gimbal); penuh dengan.\n
ākirati: menaburkan, menyebarkan, menebarkan, memercikkan, menghamburkan, membubuhkan, mengisi, menumpuk, menimbun.\n
ākoṭita: (pp dari **ākoṭeti**) telah diperas, dipukul, dibenturkan, diketuk, ditekan, dipalu, diratakan, disaring.\n
āgacchati: datang ke, mendekati, pulang atau kembali, tiba, datang kembali; mencapai, menghasilkan, pantas menerima; mampir, dipahami sebagai, merujuk atau dirujuk oleh, dipahami, dimaksudkan; kaus. **āgameti** membuat seseorang atau sesuatu datang; tunggu, berhenti; menunggui, menyambut.\n
āgata: (pp dari **āgacchati**) datang, tiba, mencapai, sampai, berhasil, terjadi; memahami; yang diwariskan secara turun temurun.\n
āgantuka: a.  datang, tiba, pendatang (baru), tamu, pengunjung; kebetulan, tak tetap, kadang-kadang; aksesori, tambahan.\n
āgama: m.  kedatangan, pendekatan, hasil; yang telah datang secara turun-temurun, sumber, acuan, sumber acuan, naskah, kitab suci; peraturan, praktik, tata krama, pematuhan; makna, pemahaman; pembayaran kembali; sisipan atau imbuhan. [agama ← Skt. āgama]
āgamma: adv.  setelah datang pada, sehubungan dengan, berdasarkan pada, berkat (_Bhagavantaṁ āgamma mahāpajāpati gotamī buddhaṁ saraṇaṁ gatā _berkat Sang Bhagawan [karena Sang Bhagawanlah], Mahapajapati Gotami berlindung kepada Buddha), dikarenakan, melalui, berkaitan dengan, dengan memakai, melalui, terhadap. ( = **ārabbha, sandhāya, paṭicca**)
āghāta: m.  kemarahan, niat jahat, kebencian, kedengkian, dendam.\n
āghātana: nt.  pembunuhan, pembantaian, pemukulan, penghancuran, pemusnahan; kematian; keadaan kacau berantakan; rumah jagal; tempat pembantaian, tempat pelaksanaan hukuman mati.\n
ācamati: menyerap air, mencuci; kaus. **ācameti** berkumur, mencuci mulut; membersihkan dari, mencebok; menghisap (kembali); **ācamāpeti** membuat seseorang membersihkan diri.\n
ācarati: mempraktikkan, melakukan, berbuat, bertindak, biasa; menginjaki, menapaki, melewati, melalui.\n
ācariya: m. guru, pakar.\n
ācariyaka: m.  guru.\n
ācāra: m.  perilaku, tingkah laku, tindak-tanduk, praktik, perilaku yang baik (pantas), kelakuan yang patut, tata krama yang baik, perangai, tingkah langkah, tingkah perangai, perbuatan, sepak terjang, sopan-santun, etiket;  a. bertindak, bertingkah, berperilaku, berbuat.\n
ācikkhati: menceritakan, memberitahu, menguraikan, memaparkan, menjelaskan, menuturkan.\n
ācikkhana: a.  memberi tahu, memaklumkan, mengumumkan.\n
āciṇṇa: (pp dari **ācarati**) dipraktikkan, dilakukan, terbiasa, lazim.\n
ājānāti: paham, memahami, mengetahui, mempelajari.\n
ājīva: m.  mata pencaharian, penghidupan.\n
ājīvaka (ājīvika): m.  petapa telanjang.\n
āṇattika: a.  berdasarkan perintah atau suruhan.\n
āṇā: f.  perintah, titah, otoritas, kekuasaan, wewenang, kewibawaan.\n
āṇāpeti: memerintahkan, memberi perintah, memerintahkan seseorang untuk menghadap, memanggil menghadap, memesan.\n
ātāpin: a.  semangat, menggebu-gebu, gigih, antusias, tekun berupaya.\n
ātura: a. sakit, berpenyakit, gering, tidak enak badan; malang, sengsara, menderita.\n
ādāti: mengambil (untuk diri sendiri).\n
ādāna: nt.  pengambilan, penggenggaman, kemelekatan (terhadap dunia), penyantapan (makanan).\n
ādāya: setelah mengambil atau menerima atau melakukan; sambil membawa, mengusung, mengambil, menggunakan, menerima; termasuk.\n
ādi: a.  pertama, utama, mulai dengan;  nt. dan seterusnya;  m.  awal.\n
āditta: m.  menyala, membara, terbakar, berpijar.\n
ādibrahmacariyaka: a.  kehidupan luhur yang unggul.\n
ādiyati: mengambil, menggenggam, mencengkam, mengambil untuk diri sendiri, memperhatikan, mengindahkan; terbelah, tercerai-berai, pecah.\n
ādisati: memaklumkan, memberi tahu, menunjukkan, perihal, merujuk ke; mempersembahkan; ger. **ādissa**.\n
ādīnava: m.  keadaan merugikan, bahaya, ketidakberdayaan.\n
ādeyya: a.  diterima; anādeyyavācā ucapannya tidak dihiraukan.\n
ādhāra: m.  wadah, penampung, “pemegang”, penopang, tumpuan.\n
ādhāvati: berlari menuju, berlari mndekat, berlari mengejar.\n
ādhipateyya (ādhipacca): nt.  kekuasaan, kedaulatan.\n
ānañja: (**ānejja, āneñja**) a.  kokoh, kukuh, tak tergoyahkan.\n
ānaya: a.  dibawa.\n
ānāpāna: nt.  **(āna + apāna)** napas masuk dan keluar; **~sati** penegakan satu atau penyadaran terhadap napas masuk dan napas keluar.\n
ānisaṁsa: m.  terpuji, manfaat, faedah, guna, hasil, kemaslahatan, berkah, keuntungan, bonus.\n
ānubhāva: m.  = **anubhāva**
āneti: membawa, membawa menuju, mengambil, meraih, menyampaikan, membawa kembali.\n
āpajjati: mencapai, tiba di, bertemu dengan, mengalami, membuat, menghasilkan, menunjukkan.\n
āpaṇa: m.  pasar, toko, kedai.\n
āpaṇika: m.  penjaga toko, pedagang, pemilik toko.\n
āpatti: f.  pelanggaran (winaya).\n
āpadā: f.  musibah, malapetaka, bencana, kemalangan, kesukaran.\n
āpanna: (pp dari **āpajjati**) dimasuki, dimulai, terjerumus ke dalam, dipenuhi dengan, telah melakukan (pelanggaran); tak beruntung, malang, menyedihkan.\n
āpātha: m.  lingkup, cakupan, jangkauan, rentang, fokus, medan (kesadaran atau persepsi), bidikan, penampakan; **~gata** masuk dalam lingkup atau fokus (bidikan), tampak, muncul.\n
āpādikā: f.  perawat, pengasuh.\n
āpādeti: (kaus. dari **āpajjati**) menghasilkan, menelurkan, mengakibatkan, menimbulkan.\n
ābādha: m.  sakit, penyakit.\n
ābharaṇa: nt. yang dipakai atau dikenakan yakni hiasan atau dandanan.\n
ābhidosika = abhidosika: 
ābhujati: menekuk, melipat, condong terhadap, mengerut.\n
ābhoga: m.  ide, pikiran, suasana batin, kecondongan batin, sangkaan.\n
āma: 1. ya, tentu saja; 2.  a.  mentah, belum diolah, belum dibakar, belum dimasak;  nt.  daging mentah; **~gandha** bau bangkai.\n
āmaṭṭha: (pp dari **āmasati**) disentuh, diraba, dijamah.\n
āmanteti: memanggil, menyapa, berbicara, menegur, berkata, berucap, berujar, mengundang, berkonsultasi.\n
āmalaka: m.  (buah) malaka, kemloko (_Phyllanthus emblica_). [malaka ← Skt. āmalaka]
āmasati: menyentuh, menyinggung, memegang, meraba, menjamah.\n
āmasana: nt.  penyentuhan, pemegangan, sentuhan, penjamahan, perabaan.\n
āmisa: nt.  daging mentah; sesuatu yang mentah atau belum diolah; jasmaniah, material, fisik, materi; makanan, makanan untuk kenikmatan, makanan lezat; umpan; keuntungan, perolehan, pendapatan, imbalan, uang, tip (persen); kenikmatan; keserakahan, nafsu.\n
āya: m.  pintu masuk; pemasukan, perolehan; lotere.\n
āyati: f.  masa mendatang, kelak kemudian hari; **itonāyati**  sejak kini.\n
āyasa: a.  terbuat dari besi.\n
āyasmant: a.  yang telah berusia, yang sepuh; _Yang Mulia_.\n
āyācati: memohon, meminta, memohon dengan sangat; meminta berulang-ulang, mendesak; berjanji, berkaul, bersumpah.\n
āyāti: datang ke sini, datang mendekat, menghampiri, datang pada.\n
āyāma: m.  membentang, merentang, menjangkau; panjang; hidup, vitalitas.\n
āyu: nt.  usia, umur; umur panjang, daya hidup.\n
āyudha (āvudha): nt.  senjata.\n
āyūhati: memajukan, mendorong, mengarah pada, menuju, , berusaha, berupaya, berjuang, tertarik untuk, memupuk, mengerahkan, mengejar, melakukan, menggiatkan.\n
āyūhana: a. nt.  berupaya, berjuang, berusaha, mengerahkan, memobilisasi, memajukan, mendorong, mengejar.\n
ārakkha: m.  menjaga, melindungi, merawat, berjaga-jaga.\n
āraññika: (= **araññaka, āraññāka, āraññaka**) a.  terpencil, di hutan, terasing, hidup di hutan, gemar menyendiri, hidup sebagai petapa.\n
āraddha: (pp dari **ārabhati**) yang telah dimulai, diawali, mulai melakukan, berketetapan hati, bertekad, kukuh, mengusahakan, gigih; **~viriya** nt. gigih penuh semangat, penuh semangat..\n
ārabbha: (ger. dari **ārabhati**)  mengawali, memulai; berawal dengan, bertitik-tolak dari, dengan merujuk pada, berkenaan dengan, perihal; **~vatthu** kesempatan untuk berupaya, kewajiban, keprihatinan.\n
ārabhati (ārabbhati)  : 1. memulai, mengawali, mulai melakukan, berusaha. (_viriyam ārabhati_  gigih berupaya/bersemangat); 2. membunuh, menghancurkan.\n
ārambha: m.  upaya, usaha, inisiatif, prakarsa, mulai; sokongan, landasan, objek, hal, kerepotan.\n
ārammaṇa: nt.  “landasan”, penopang, pembantu, pijakan, tumpuan, sarana, basis, sandaran, kesempatan; kondisi, sebab, penyebab; objek indriawi, objek pikiran atau kesadaran, objek; ditopang oleh, bersandar pada, terpusat, terfokus pada.\n
ārādhanīya: a.  dicapai, diraih, berhasil.\n
ārādheti: membuat senang, mengambil hati, meyakinkan; mencapai, meraih, berhasil, mewujudkan.\n
ārāma: m.  kesenangan, kegembiraan; tempat bersenang-senang, taman, tempat hiburan, tempat pelesiran; wihara, tempat tinggal para bhikkhu (meliputi bangunan serta pekarangannya).\n
ārāmika: a.  gemar akan, suka akan; milik atau berkaitan dengan suatu ārāma, pelayan ārāma.\n
ārūḷha: (pp dari **āruhati**)  naik, terbit, lanjut sampai, muncul, ditimbulkan, terjadi, dibuat, dilakukan.\n
āruhati: memanjat, naik, terbit, menaiki, mendaki.\n
ārogya: nt.  tiada sakit, sehat.\n
ārocāpeti: (kaus. II dari **āroceti**)
āroceti: memberi tahu, menceritakan, mengumumkan, berbicara kepada.\n
āropeti: menaikkan, naik sampai; mengenakan, mempercayakan kepada, menghasilkan, mengadakan,membuat, menyiapkan, memperlihatkan, menceritakan, memberikan; **vādaṁ ~**membantah, memperoleh yang lebih baik daripada (gen.).\n
ālaggeti: menggantungkan pada, menempelkan pada, mengikatkan pada.\n
ālapati: berkata.\n
ālapana: nt.  hal bercakap-cakap, mengobrol, berbicara; sapaan, tegur-sapa, sebutan, panggilan, vokatif, percakapan, pembicaraan, seruan.\n
ālaya: m. nt.  tempat tertengger, tenggeran; kediaman, hunian; kemelekatan, keinginan, kemelengketan, nafsu keinginan, hal menggelayuti; dalih, helat, kepura-puraan, tipu daya.\n
āloka: m.  penglihatan, pemandangan, pandangan; cahaya terang, benderang; penglihatan jelas, cahaya batin, celik batin; kecemerlangan; **~sandhi**m. f.  lubang pengintip, jendela.\n
ālokita: (pp dari **āloketi**)  nt. memandangi, melihat pada, melihat ke depan.\n
āḷavaka (āḷavika): a.  yang tinggal di hutan, penghuni hutan, yang tinggal di Kota _Āḷavī_.\n
āḷimpeti: 1. melumuri, mengolesi; 2. menyalakan (api), membakar.\n
āḷhaka: m. nt.  ukuran volume (takaran) untuk cairan atau benda kering; = 4 **pattha**; (Skt. **āḍhaka**).\n
āvajjati: merenungkan, memperhatikan, mengindahkan, memaling ke, menangkap (suara), mendengarkan; menyingkirkan, membalikkan, menumpahkan; kaus. **āvajjeti**.\n
āvajjana: nt.  hal memalingkan / memalis ke, memperhatikan, mengamati.\n
āvaṭa: a.  tertutup, terselubung, terlarang, kedap terhadap.\n
āvaṭṭa: a. berputar, melingkar, berpelintir; diputar, diubah, digoda; pusaran air; keliling.\n
āvaraṇa: a. menutupi, menahan; nt. rintangan, halangan, hambatan, tirai; perintang, penghambat, penghalang.\n
āvali: f.  baris, jajaran.\n
āvasati: hidup di/dalam, menghuni, berdiam, menetap.\n
āvasatha: m.  tempat tinggal, permukiman, kediaman, rumah.\n
āvaha: a.  membawa, mendatangkan, menimbulkan, memunculkan, menghantarkan.\n
āvāsa: m.  persinggahan, kediaman (para bhikkhu), rumah, permukiman; kompleks bangunan yang terdiri dari balai uposatha, ruang makan, ruang sauna, kamar tinggal (wihara), bilik kediaman (tunggal atau sederet).\n
āvāsika: a.  berdiam di, menghuni di rumah, penghuni tetap.\n
āvāha: m.  'mengambil sang gadis' (_kaññā-gahaṇaṁ_); perkawinan, pernikahan.\n
āvi: adv.  jelas, terungkap, nyata, terbuka, di depan mata, tampak.\n
āvikamma: nt.  hal membuat jelas, mengungkapkan, menyingkapkan, menyatakan, menjelaskan.\n
āvikaroti: memaklumkan, menunjukkan, menjelaskan, mengungkapkan.\n
āvijjhana (āviñjana, āviñchana): a.  melingkupi, bergelayut, bergelantungan; bersentuhan dengan; menuju; menarik, menyeret, menghela.\n
āvuta: 1. (pp dari **āvuṇāti**) terikat, ditenun, terpancang pada; disulakan, ditancap; 2. tertutup, tersumbat, terhalang.\n
āvudha (āyudha): nt.  senjata, alat untuk bertarung.\n
āvuso: vok. pl. m. (bentuk ringkas dari **āyusmanto**) yang terhormat, panggilan akrab sesama bhikkhu terutama bhikkhu senior terhadap bhikkhu junior, atau panggilan akrab bhikkhu terhadap umat awam.\n
āvenika: a.  spesial, khusus, istimewa, luar biasa, khas, unik.\n
āveḷa: a.  melingkar, memancar, mencuat.\n
āveḷā:  f.  bunga  hiasan telinga, subang.\n
āsajja:  (grd. **āsādeti**)  duduk di, pergi ke, menghampiri, bertempatkan, termasuk ke, dekat; memasang pada, menghantam, menyerang, memukul, menongkrongi, berkutat pada, dengan gigih, secara spontan.\n
āsatti: f.  kemelekatan, ketergantungan terhadap.\n
āsana: nt.  hal duduk, tempat duduk, bangku.\n
āsanna: a.  dekat.\n
āsaya: m.  kediaman, tempat yang sering dikunjungi, jelajahan, naungan, penampung, sandaran, penyokong, penopang, kondisi; kecondongan, kecenderungan, niat, hasrat, harapan; leleran, eksresi.\n
āsava: m.  yang mengalir masuk atau keluar; minuman keras (cairan memabukkan yang merupakan ekstrak atau sekresi dari suatu pohon atau bunga); leleran nanah; kotoran batin, leleran batin.\n
āsādeti: (kaus. dari **āsādati**)  menangkap, menyentuh, menghantam, menyerang; menghampiri, mendekati.\n
āsīvisa: m.  ular.\n
āsevati: mengakrabi, mengunjungi, berlatih, mempraktikkan, mengikuti, menurutkan, menikmati, menggemari.\n
āsevana: nt.  1. praktik; hal mengikuti, menuruti, atau menggemari; 2. hal berulang-ulang, sambung-menyambung.\n
āha: ia berkata.\n
āhacca: 1. (ger. dari **āhanati**); 2. (ger. dari **āharati**) telah dilepas, dapat dilepas(kan); melantunkan, disitir, dikutip, dicuplik, pendarasan.\n
āhaṭa: (pp dari **āharati**)  dibawa, diperoleh.\n
āhata: (pp dari **āhanati**)  dihantam, dipukul, didera, digebuk, dilanda, dipengaruhi oleh; **~citta** nt. batin yang dirundung kebencian, dendam.\n
āhanati: memukul, menghantam, menggebuk, mendera, menyentuh.\n
āharaṇa: nt.  hal membawa.\n
āharati: mengambil, menggenggam, mengeluarkan, membawa pergi, membawa, menangkap, menjatuhkan (menurunkan), memperoleh, menerima, mendapatkan, menimbulkan, mendatangkan, membawa menuju, melibatkan diri dalam, menyentuh, berpaling kepada; menyerang; mencuplik, menyitir, merujuk ke.\n
āhāra: m.  makanan.\n
āhārūpahāra: m.  konsumsi makanan, penyantapan makanan, hal makan; urusan serah terima, urusan.\n
āhiṇḍati: berkelana, mengembara, dinas, sedang sibuk dalam.\n
āhita: a.  yang telah dimasukkan˴ ditaruh; yang telah dimasukkan dengan bahan bakar, yang terbakar.\n
āhuṇa: nt.  penghormatan, persembahan.\n
āhuneyya: a.  layak/patut menerima persembahan atau buah tangan.\n
ikkhaṇika: m.  peramal, penujum, penilik, cenayang.\n
iṅgha: hayo, ayo, coba, tolong (partikel bernada mendesak, memperingati).\n
icchatā: f.  keinginan, pengharapan, hasrat.\n
icchati: ingin, berniat, hendak, memohon, minta, mengharapkan, condong pada, menganut, bersikukuh.\n
icchā: f.  keinginan, pengharapan.\n
iṭṭha: (pp dari **icchati**) menyenangkan, berkenan di hati, sejahtera; nt. kesejahteraan, kondisi baik, kesenangan, kebahagiaan.\n
iṭṭhakā (itthakā): f.  batu bata, ubin (genteng).\n
itara: a.  yang lain, yang kedua, yang berikut, yang berbeda; **itarītara**satu atau lainnya, apa pun, siapa pun.\n
iti: (=**ti**) demikian(lah); **iccādi**dan sebagainya.\n
itivuttaka: nt.  ‘demikianlah yang diutarakan’, (kitab) kutipan; judul buku keempat dari _Khuddaka-nikāya_; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**).\n
ito: dari sini, dari ini; (di) sini; sejak sekarang, sejak dari, semenjak, dari sekarang, setelah ini, oleh karena itu.\n
itthatta: nt. keadaan sekarang ini, hidup ini, keberadaan (eksistensi) ini; kewanitaan, kefeminian.\n
itthaṁ: demikian, dengan cara ini; **~nama** bernama demikian, dipanggil demikian, disebut demikian, dinamai demikian.\n
itthi (itthī): f.  wanita, perempuan, istri;  **~dhana**nt. harta istri, maskawin, mahar. [istri ← Skt. strī]
itthikā: f.  wanita.\n
idāni: kini, sekarang, baru saja.\n
iddha: (pp dari **ijjhati**)  berhasil, sukses, gemilang; kaya, makmur, berkecukupan.\n
iddhi: m.  ‘daya’; kemampuan, kekuatan; daya gaib; kondisi, keadaan, posisi, pengaruh serta kekuatan yang unggul atau baik; keberhasilan; **~pāṭihāriya**nt.  mukjizat kekuatan gaib;  **~pāda** m. nt. sarana keberhasilan, landasan kemampuan gaib, landasan daya batin; **~visaya**m. rentang atau jangkauan daya (gaib).\n
iddhimant: a.  berkemampuan, berhasil, berjaya; memiliki daya gaib.\n
idha: adv.  di sini, di dunia ini, dalam kelahiran ini, dalam hubungan ini, dalam kaitan ini, _sehubungan dengan ini_, baru saja, sekarang, akhir-akhir ini; _punar idhāgato_  kembali ke dunia ini lagi.\n
inda: 1. Dewa Indra; 2. pemimpin, tuan, raja; **~ khīla**m.  tonggak Indra, tonggak di atau di depan gerbang kota, tonggak yang ditancapkan di depan pintu masuk rumah; **~ gopaka**m.  sejenis serangga berwarna merah, semacam belalang, kumbang kecil (_lady-bird/bug_) yang akan keluar dari tanah sehabis hujan, laron.\n
indriya: nt.  dasar pengendali, kekuatan pengarah; fungsi, kemampuan, kecakapan, daya, daya pengendali, indra (bukan organ); jenis, ciri, roman, azas penentu, tanda; jenis kelamin; kekuatan utama, kekuatan pengendali; kategori. [indra/indria ← Skt. indriya]
iriyā: f.  gerakan, sikap badan, tingkah laku; **~patha** m. cara berperilaku, cara bertingkah laku, cara bergerak, tindak-tanduk, perilaku baik, gerakan, sepak terjang, gerak-gerik, sikap.\n
isi: m.  orang suci, orang kudus, resi; sepuluh penggubah atau pelantun kidung Weda (_Aṭṭhaka_, _Vāmaka_, _Vāmadeva_, _Vessāmitta_, _Yamataggi_/ _Yamadaggi_, _Aṅgirasa_, _Bhāradvāja_, _Vāseṭṭha_, _Kassapa_, _Bhagu_); **~sattama** tujuh orang suci (_Vipassin_, _Sikhin_, _Vessabhu_, _Kakusandha_, _Koṇāgamana_, _Kassapa_, dan _Gotama_). [resi ← Skt. ṛṣi]
issara: m.  tuan, penguasa, juragan, majikan, bos, pemimpin; dewa pencipta, Tuhan, Sang Pencipta, Dewa Brahma.\n
issariya: m.  daya kekuasaan, kekuasaan; _issariyaṁ kāreti_  berkuasa atas.\n
issā: f.  iri hati; **~pakata**a. diliputi iri hati, penuh iri hati, berwatak suka iri hati, dilanda iri hati.\n
issukī: a.  iri hati.\n
iha: adv. sini; **tasmātiha**oleh karena itu di sini.\n
īti (ītī): f.  penyakit, malapetaka, bencana, wabah, gangguan, kesukaran.\n
ukkaṇṭhati: mendambakan, tak puas, cerewet.\n
ukkaṇṭhita:  (pp dari **ukkaṇṭhati**)  tidak puas, cemas, menyesal, mendambakan, cerewet, kesal, jengkel, dongkol.\n
ukkā: f.  bara api, nyala api, obor; perbaraan, perapian, tungku, anglo.\n
ukkujjeti (ukkujjati)  : membalikkan kembali, menegakkan kembali, meluruskan kembali.\n
ukkuṭika: m.  sejenis cara jongkok; setengah jongkok; jongkok dengan tumit terangkat dari tanah dan kedua siku diletakkan di atas lutut.\n
ukkhitta: (pp dari **ukkhipati**)  diambil, diangkat, dibekukan (diskors), ditunda, ditangguhkan, digantungkan); diterbangkan.\n
ukkhipati: mengangkat, menyingkap, mengambil, membekukan (menskors, menangguhkan); **sīsaṁ ~** menganggukkan kepala.\n
ukkheṭita: a.  diludahkan, disemburkan, dilontarkan, dibuang.\n
uggacchati: naik, terbit.\n
uggaṇhāti: mengambil, memperoleh, mempelajari, menguasai.\n
ugghāṭeti: mengambil, melepaskan, menghilangkan, mengakhiri.\n
ucca: a.  tinggi.\n
uccāra: m.  kotoran, berak, tahi, feses, tinja; _uccāraṁ gacchati_  berak, membuang air besar.\n
uccāranā: f. nt.  hal mengangkat naik, menerbitkan, mencetuskan; hal bersuara.\n
uccāreti: mengangkat, mengangkat tinggi-tinggi, menjunjung.\n
uccāliṅga: m.  cacing perut, **~pāṇaka** m. ulat bulu atau cacing-cacingan (= **lomasapāṇaka**).\n
uccāvaca: a.  tinggi dan rendah, aneka, beragam, berbagai.\n
uccināti: mengumpulkan, memilih, mencari, memungut.\n
ucchindati: menghancurkan, meluluhlantakkan, membinasakan.\n
ucchu: m.  tebu (_Saccharum officinarum_).\n
uccheda: m.  penghancuran, pemotongan, pemutusan, pelenyapan, pencerai-beraian, kemusnahan/ pemusnahan; **~vāda**a.  yang berpaham bahwa setelah seseorang meninggal segalanya pun tamat sudah (tiada kelahiran kembali), yang menganut paham kemusnahan, annihilasionis.\n
uju (ujju): a.  lurus, tegak, langsung; jujur, sadik, mustakim.\n
ujjalana: nt.  hal menyalakan (pelita).\n
ujjhaggati (ujjagghati): menertawakan, terbahak-bahak, tergelak-gelak, mengejek, mencemoohkan, memperolok-olokkan, mempersendakan.\n
ujjhāpeti: (kaus. dari **ujjhāyati**)  menggoda, mengganggu, mengusik, menyakitkan hati, menjengkelkan, mendongkolkan, mengesalkan, mengeluh, mengadu kepada.\n
ujjhāyati: terusik, terganggu, menjadi jengkel atau kesal, mendongkol, menggerutu; mencibir, mencemooh, memandang rendah.\n
uñcha (uñchā): f.  apa saja yang dikumpulkan untuk dijadikan makanan, mengumpulkan sedikit demi sedikit; hal merapu makanan [memunguti (barang-barang yang terbuang atau tidak berguna); meminta sedekah].\n
uṭṭhahati (uṭṭhāti): berdiri, bangkit, bangun, muncul, mencuat, dihasilkan, bangkit berupaya.\n
uṭṭhāpeti: (kaus. dari **uṭṭhahati**)  membuat naik (terbit, bangun); menaikkan; menyiapkan atau memperlengkapi (dengan); menyanjung, memuji; mengusir (seseorang), mengangkat.\n
uṇha: a.  panas, hangat.\n
utu: m. nt.  waktu (yang baik atau sesuai), musim, iklim; panas, suhu, kalori; masa subur.\n
uttanta: ketakutan, pingsan.\n
uttama: a.  “yang ter”, tertinggi, terbesar, terbaik, adiluhung, utama. [utama ← Skt. uttama]
uttara: a.  lebih tinggi, tinggi, atas, superior; utara; berikut, selanjutnya; lebih. [utara ← Skt. uttara]
uttarati: keluar dari (air), melintasi, mengalir, meluap, menjelajahi, menyebar, mendidihkan, menyeberangi, mengarungi, melampaui, membentangkan.\n
uttarattharaṇa: nt.  kain penutup/alas ranjang atau kursi, seprai.\n
uttarāsaṅga: m.  jubah atas.\n
uttari (uttariṁ): melebihi, unggul, tambahan, lanjut; **~bhaṅga**nt. jatah (bagian) ekstra, kudapan, makanan kecil; **~manussadhamma**m.  kualitas yang mengungguli manusia biasa, kemampuan lebih terhadap manusia awam; pencapaian daya supramanusia.\n
uttasati: membuat takut, diperingati atau ditakuti, menjadi ketakutan.\n
uttāna: a.  terentang, terjengkang; jelas, terbuka, nyata; dangkal; **~mukha** berbicara jelas, mudah dipahami, berwajah terbuka; **~seyyaka** “berbaring telentang”, bayi..\n
uttāreti: (kaus. dari **uttarati**)  mengeluarkan, mengangkat keluar, mengentas.\n
udaka: nt.  air, perairan.\n
udagga: a.  tertinggi, tinggi; sangat gembira, agung, mulia, bahagia, melonjak.\n
udañjala~ṁ kīḷati: bermain air.\n
udadhi: m.  samudra, lautan.\n
udapādi: (aor. 3rd sg. dari **uppajjati**)  muncul, menjadi, terlahir, terbit.\n
udapāna: m. sumur, telaga, waduk.\n
udara: nt.  perut; ruang, lubang, rongga, bagian dalam;  **~vaṭṭi**kantung perut, perut.\n
udāna: nt.  ungkapan suasana hati dalam wujud sajak, ungkapan ketergugahan hati, ungkapan sukacita; judul kitab ketiga dari Khuddaka -nikāya; salah satu ragam kitab suci (▶ **navaṅgabuddha-sāsana**).\n
udāneti: mencetuskan, mengungkapkan.\n
udāharaṇa: nt.  contoh, misal.\n
udāhāra: m.  ungkapan, ucapan, tuturan, khotbah, wejangan, pernyataan.\n
udukkhala: m. nt.  lesung, lumpang.\n
uddasseti: memperlihatkan, menampakkan, mempertunjukkan.\n
uddāna: nt.  rangkuman, ringkasan, ikhtisar.\n
uddiṭṭha: (pp dari **uddisati**) telah ditunjukkan, ditunjuk, dipaparkan, dibabarkan, diajukan, dikemukakan, , digariskan, dirumuskan; ditujukan.\n
uddisati: mengajukan, menunjukkan, menunjuk, membagikan; menetapkan, melimpahkan.\n
uddissa: setelah ditunjukkan oleh, dengan tanda-tanda atau indikasi (petunjuk); menunjuk pada, mengarah pada, ditujukan kepada; terhadap, kepada; dengan mengacu pada, karena, sehubungan dengan, berkaitan dengan, atas nama; dengan tujuan.\n
uddesa: m.  pemaparan, penguraian, pelantunan, pengulasan, penjelasan, rincian, seluk-beluk; acuan; pendarasan.\n
uddhaṁ: tinggi, di atas, atas, di puncak; mendatang, di masa depan, karena itu, dari itu; **~mukha** adv. menghadap ke atas/hulu.\n
uddhacca: nt. kegelisahan, agitasi, gangguan, batin yang meluap-luap, hal terangsang.\n
uddhana: nt.  tungku, anglo, tanur, perapian, perbaraan.\n
uddharaṇa: nt.  pengambilan, pengangkatan, penaikan, penarikan (keluar).\n
uddharati: menaikkan, terbit, mengangkat; terlampau naik, mengguncang; mengambil, mencabut, menyingkirkan; menarik keluar.\n
undura: m. tikus.\n
unnamati: naik, menaik, menegakkan.\n
unnāmin: a.  naik, menaik.\n
upakacchaka: m.  seperti sebuah cekungan atau lekukan, seperti ketiak, seperti lubang, ketiak, pangkal paha.\n
upakaṭṭha: a.  mendekati, hampir.\n
upakaḍḍhati: menyeret, menghela, menarik (menuju), menjerumuskan.\n
upakappati: bermanfaat untuk, (bisa) sampai pada.\n
upakaraṇa: nt.  bantuan, layanan, dukungan, sarana mempertahankan hidup, penghidupan.\n
upakāra: m.  pelayanan, bantuan, manfaat, kewajiban, pertolongan, kemurahan hati.\n
upakkama: m.  hal menuju, pergi ke, mendekati, menghampiri, menyerang, menerapkan, mengenakan; melakukan, bertindak, melangsungkan, tindakan; cara, sarana, upaya, jalan, jalan yang bijaksana, jalan keluar, muslihat, cara jahat, persekongkolan.\n
upakkamati: mengawali, memulai, menyerang, melakukan, berupaya, berusaha, berikhtiar.\n
upakkilesa: m.  kotoran batin, cemaran batin, noda batin.\n
upaga: a. mencapai, sampai pada, mengalami, yang dihasilkan, yang dimiliki, berada dalam (_yathā-kammūpaga_ keberadaan yang sesuai dengan perbuatan; berada dalam kondisi sesuai perbuatan (lampau) mereka).\n
upagacchati: datang ke, pergi ke, menghampiri, mengalir ke; menjalani, mengalami, memulai, melangsungkan.\n
upagata: (pp dari **upagacchati**) pergi ke, datang, menghampiri; mengalami, menjalani, menderita, dilanda.\n
upacāra: m.  mendekati, jalan masuk; daerah seputar; kebiasaan, praktik, perilaku; jalan, cara penerapan, penggunaan; perhatian, kehadiran, kesopanan, perilaku sopan; hampir, menuju.\n
upacikā: f.  rayap, anai-anai.\n
upacita: (pp dari **upacināti**)  tertumpuk, terkumpul, dihasilkan, dilestarikan, disimpan, dibangun.\n
upacitatta: nt.  penimbunan, pengumpulan.\n
upacchindati: memutuskan, memotong, memisahkan, menceraikan, menghancurkan, menyela, menghentikan.\n
upaccheda: m.  pemutusan, penghancuran, pengakhiran, penghentian.\n
upajīvin: a. hidup mengandalkan, bertahan hidup dengan.\n
upajjha= upajjhāya: 
upajjhāya: m.  guru spiritual, guru pelantik (menjadi bhikkhu), guru pemberi sila, guru pembimbing setelah diterima sebagai seorang bhikkhu (ke dalam Sanggha), mentor.\n
upaṭṭhapana: nt.  hal menyediakan, menyiapkan.\n
upaṭṭhapeti (upaṭṭhāpeti): (kaus. dari **upaṭṭhahati**)  menyediakan, memperoleh, mendapat, menyiapkan, menawarkan, memberi; menghadirkan, menyuruh dilayani atau dirawat; menggaji, mengupahi (seorang pelayan)
upaṭṭhahati (upaṭṭhāti): berdiri dekat, menunggui, melayani, merawat, menyokong, menopang; muncul, mencuat, terjadi, hadir; memahami.\n
upaṭṭhāka: m.  pelayan (pribadi), abdi; **~kula** nt. keluarga pelayan, keluarga pengabdi, keluarga penyokong (penopang), dayaka.\n
upaṭṭhāna: nt.  pelayanan, pengabdian, perawatan, pemeliharaan, peladenan, hal menyertai; sembahyang; balairung, balai besar; pemahaman, pengertian.\n
upaṭṭhita: (pp dari **upaṭṭhahati**) yang telah disiapkan, dilayani, disediakan; siap; yang dihormati dengan; tiba, mencapai, muncul, hadir, ada.\n
upaṭṭheti: (kaus. dari **upaṭṭhahati**) menyuruh melayani, menyokong; **upaṭṭhessati**menempatkan, memasang.\n
upatiṭṭhati: berdiri dekat, merawat, mengagungkan, memuliakan, menjunjung tinggi.\n
upatta: a.  berlumuran, bergelimang, teroles.\n
upatthaddha: (pp dari **upatthambhati**)  kaku, tegang, mengeras; ditopang, disangga, bertumpu pada, bersandar pada.\n
upatthambha: m.  penyokong, penguat, penopang, sangga, tiang, saka (guru); ereksi; kelegaan, peredaan; dorongan (semangat).\n
upatthambheti: (kaus. dari **upatthambhati**) memperkokoh, menopang, memperkuat, menyokong, menyangga.\n
upadesa: m.  hal menunjukkan, instruksi, nasihat, uraian, penjelasan, wejangan, penuntun, tuntunan.\n
upaddava: m.  ‘melanda’; musibah, geruh(-gerah), kegeruhan, malapetaka, kesusahan, rintangan.\n
upaddavati: mengganggu.\n
upadduta: (pp dari **upaddavati**)  dilanda, diserbu, diserang, ditindas, diganggu, diusik, ditaklukkan, menderita.\n
upadhāraṇa: nt.  “penampung”, ember susu, kokoh, mantap.\n
upadhi: m.  meletakkan (di bawah), landasan, substansi, materi, bahan dasar (baku), fondasi (kelahiran kembali); kemelekatan terhadap kelahiran kembali; objek kemelekatan.\n
upanāmeti: membungkuk terhadap, menempatkan berlawanan atau dekat dengan, menghampiri, membawa dekat; mempersembahkan, memberikan.\n
upanāyika: a.  menunjuk ke, berkenaan dengan, mengenai; menjelang (memasuki).\n
upanāha: m.  niat jahat, dendam, kebencian, rasa permusuhan.\n
upanikkhitta: a.  ditaruh (secara sembunyi-sembunyi), ditempatkan dekat atau di atas;  m. mata-mata.\n
upanikkhipati: menyimpan dekat.\n
upanijjhāyati: merenungkan, mengingat-ingat, memenungkan, memandangi, mengkhayalkan, mengenang-ngenangkan, membayang-bayangkan.\n
upanidhi: f.  timbunan, simpanan; cagar, benda tanggungan, jaminan; perbandingan;  _upanidhiṁ na upeti _tak dapat diperbandingkan.\n
upanipajjati: berbaring dekat dengan, berbaring di atas.\n
upanisīdati: duduk dekat dengan atau pada.\n
upanissāya: (ger. dari **upanissayati**) adv.  dekat, bergantung pada, dengan atau melalui.\n
upaneti: membawa menuju, menimbulkan, mengakibatkan, menyodorkan, memberikan, menghadirkan; diakhiri; dibawa serta, dibawa pergi.\n
upapajjati: membawa ke, terlahir di, berasal, muncul, mencapai.\n
upapatti: f.  kelahiran, kelahiran kembali; kesempatan; objek yang sesuai.\n
upaparikkhati: mencermati, menyelidiki.\n
upapāta: m.  kelahiran; kelahiran kembali.\n
upabrūhaṇa: nt.  ekspansi, perluasan, pertambahan, pengembangan, tambahan, penguatan.\n
upabhoga: m.  kenikmatan, keuntungan, kebutuhan, kegunaan.\n
upama: a.  “hampir”, seperti, mirip, sama (dengan). [umpama Ü Skt. upama]
uparamati: berhenti, mereda, tenang.\n
upari: di atas, di bagian atas.\n
uparima: a.  di puncak, di (bagian) atas, (tingkat) yang lebih tinggi.\n
uparodheti: (kaus. dari **uparundhati**)  menghentikan, merintangi, menyetop, menghancurkan, membinasakan.\n
upalāpeti: membujuk, merayu, memikat, mengambil hati.\n
upavāda: m.  hal mencela, mencari-cari kesalahan, menghina.\n
upavādaka: a.  mencela, mencari-cari kesalahan, berbicara buruk terhadap.\n
upasaṁharati: mengumpulkan, menyatukan, mengonggokkan; mengatur, memusatkan, memfokuskan; menggenggam, menghadirkan, menjaga, menyediakan, melayani, merawat.\n
upasaṁhita: a.  ditemani oleh, disuguhi, berkaitan dengan, ditawari, diajak.\n
upasagga: m.  1. serangan, gempuran, gangguan, bahaya; 2. prefiks, preposisi.\n
upasaṅkamati: mendekati, menghampiri, pergi menuju, mendatangi, memasuki; merawat.\n
upasama: m. kekaleman, ketenangan, keheningan, kedamaian, keredaan, _ketenteraman_.\n
upasampajjati: mencapai, memasuki, memperoleh, ditahbiskan menjadi seorang bhikkhu.\n
upasampadā: f.  pengambilan, penerimaan, perolehan, pelaksanaan; pengambilan kebhikkhuan, penahbisan menjadi bhikkhu, penerimaan menjadi bhikkhu.\n
upasampanna: (pp dari **upasampajjati**) diperoleh, didapatkan, diterima, diperoleh kebhikkhuan, diterima sebagai bhikkhu, ditahbiskan menjadi bhikkhu.\n
upassaya: m. kediaman, peristirahatan (pesanggrahan), perlindungan, suaka, perteduhan.\n
upahata: (pp dari **upahanti**) cedera, rusak, musnah, hancur, terganggu, terhambat, terhalang; **~indriya** cacat indra.\n
upahanti (upahanati): menghambat, mencederai, mengurangi, menghalangi, merusak, menghancurkan.\n
upahāra: m.  pengajuan, penawaran, pemberian, persembahan, hadiah, penghadiran.\n
upādā: adv. bergantung pada sesuatu; bukan asli, turunan, wujud sekunder (dari _rūpa_).\n
upādāna: nt.  bahan bakar, pasokan, persediaan, bekal; kemelekatan; hal menggenggam, mencengkeram.\n
upādāya: adv. berdasarkan atas, dibandingkan dengan, dengan mengacu pada, menurut, demi, selaras dengan; karena, disebabkan oleh; bergantung pada, dengan melekat pada, dengan berpegangan pada; turunan, wujud sekunder (dari _rūpa_).\n
upādiṇṇa: (pp dari **upādiyati**)  digenggam, ditangkap, diambil, digunakan; hasil (akibat) penggenggaman yakni materi, turunan, sekunder; bernyawa.\n
upādiyati: menggenggam, memegang, menempel pada, melekat pada.\n
upāyāsa: m.  kekecewaan, keputusasaan, gejolak, kehilangan harapan.\n
upāsaka: m.  umat berumah tangga, umat awam.\n
upāsikā: f.  umat awam wanita, umat berumah tangga wanita.\n
upekkhaka: a.  ketidakacuhan, kecuekan, keseimbangan batin.\n
upekkhā (upekhā, upekkhanā)  : f.  keseimbangan batin, ketidakacuhan; perasaan netral (= _adukkhamasukhaṁ_  tidak menderita pun tidak bahagia).\n
upeta: (pp dari **upeti**)  memiliki, dianugerahi, ber…..\n
upeti: pergi ke, datang pada, menghampiri, mencapai, mengalami.\n
uposatha: m.  hari Uposatha, ibadat Uposatha, sila Uposatha; **~agga** (**uposathāgāra**) tempat penyelenggaraan Uposatha, tempat pelantunan patimokkha; **~kamma** pertemuan atau upacara yang berhubungan dengan hari Uposatha; _uposathaṁ karoti_  melakukan ibadat Uposatha; _uposathaṁ upavasati_  mengamalkan Uposatha, menjalani ibadat Uposatha, melakukan puasa Uposatha (dengan menjalankan delapan sila); _uposathaṁ samādiyati_  mengambil sila Uposatha (delapan sila). [puasa/upawasa ← Skt. upavasa(tha)]
uppakka (upakka): a.  terpanggang, hangus, _gosong_, terbakar, menyelara (mengering), melayu, mengisut, mengeriput, mengerut, melisut.\n
uppajjati: lahir, muncul, hadir, terbentuk.\n
uppajjanaka: a. muncul, timbul.\n
uppaṇḍuppaṇḍukajāta: a.  pucat pasi, kekuning-kuningan.\n
uppaṇḍeti: menertawai, mengejek, berolok-olok, mencemoohkan, memperolok-olokkan, menggoda.\n
uppatati: terbang ke atas, loncat ke atas, terlontar ke atas.\n
uppatti: f.  kemunculan, hasil, kelahiran, kejadian, pemerolehan.\n
uppatana: nt. terbang, naik, loncat, lompat.\n
uppanna: a.  (pp dari **uppajjati**) terlahir kembali, muncul, terbentuk.\n
uppala: m.  teratai (biru), bunga teratai.\n
uppāda: m.  hal muncul, mengada, lahir.\n
uppādeti: (kaus. dari **uppajjati**) memunculkan, menimbulkan, menerbitkan,menghasilkan, melahirkan, mencetuskan, memperlihatkan, membuat; memperoleh, mendapatkan; mengeluarkan (darah).\n
uppilavati (uplavati): muncul (dari air), terbit, terapung; melonjak.\n
ubbaṭṭeti: melumuri, melumangkan, melumas, memolesi, mengolesi, memulas.\n
ubbandhati: menggantung (diri), mencekik.\n
ubbāḷha: a.  tertekan, terganggu, terusik.\n
ubbijjati: menjadi terganggu atau terusik, menjadi ketakutan atau kecut hati.\n
ubbedha: m.  ketinggian.\n
ubbhaṁ: di atas; **ubbhajānumaṇḍalaṁ** di atas lutut.\n
ubbhujati: berbungkuk, mengangkat (secara paksa); **ubbhujitvā**secara paksa.\n
ubhato: adv.  kedua, dua; **~vyañjanaka** berkelamin ganda; hermafrodit.\n
ubho: a.  keduanya.\n
ummattaka: a.  gila, tidak waras.\n
ummasati: menyentuh, memegang, mengangkat, meraba naik.\n
ummasanā: f.  hal mengangkat naik, meraba naik.\n
ummujjati: muncul dari, menyembul dari, keluar dari.\n
uyyāna: nt.  taman, kebun raya, taman hiburan.\n
uyyojeti: (kaus. dari **uyyuñjati**) mengupayakan, menghasut, membujuk, memecat, berpamitan kepada, mengirim, melepaskan.\n
ura: m. nt.  dada, payudara.\n
uracchada: m.  (hiasan) penutup payudara, perisai payudara.\n
ulūka: m.  burung hantu.\n
ullaṅghati: meloncat, bangkit.\n
ullaṅghanā: f.  hal meloncat naik, melonjak, naik, berbangkit.\n
ullapati: berseru, berbicara kepada, mengajukan tuntutan atas, menyerukan, mengklaim, menyatakan, berkoar tentang, menjerit.\n
ullapana: nt.  hal menyatakan, menyerukan, mengklaim, mengajak.\n
ullitta: a.  berturap atau berlepa dalam.\n
uḷāra: a.  besar, agung, mulia, luhur, bagus, kaya, hebat, ulung, unggul, baik sekali; nyata mewujud (_physically actualized_). (Menurut Dhammapāla, kata ini mengandung tiga makna : _paṇītaṁ_, _seṭṭhaṁ_, dan _mahantaṁ_.)
uḷāratta: nt.  kehebatan.\n
uḷumpa: m.  rakit, pengapung, pelampung, getek.\n
usabha: m.  sapi jantan (acapkali sebagai simbol kejantanan dan kekuatan); **puris~** pria perkasa.\n
usu: m. f.  panah.\n
usmā: f. panas.\n
ussakkati: 1. merangkak keluar atau ke atas, naik; 2. berusaha, mencoba, berupaya.\n
ussanna: a.  meluber, berlimpah, menumpuk, banyak, penuh dengan; dinobatkan; meluas, terhampar luas.\n
ussarati: berlari keluar, melarikan diri.\n
ussava: m.  pesta, kenduri, pesta pora, hari raya, _perayaan_, _festival_.\n
ussahati: mampu, cocok, berani, sanggup, kuasa, dapat; menggiatkan.\n
ussāpeti: mengangkat, menegakkan, menaikkan, mengagungkan.\n
ussāreti: 1. (kaus. dari **ussarati**) membuat pindah kembali, membuat pergi, menyurut; 2. ( = **ussādeti**) membuat berkibar, membuat terbang, mengangkat, menerbangkan.\n
ussāhita:  (pp dari **ussāheti**)  ditetapkan, dihasut, didorong, didesak.\n
ussita: (pp dari **ussāpeti**)  ditegakkan, tinggi, diangkat.\n
usseḷi: bersuit-suitan, bersorak.\n
ūna: a.  kurang, tak cukup, kekurangan; **ekūna** kurang satu.\n
ūmī (ūmi): f. gelombang.\n
ūru: m.  paha.\n
ūsa: m.  garam.\n
ūsara: a.  asin, bergaram; nt.  tanah yang asin atau bergaram.\n
ūhata: a.  terangkat; dikeluarkan, keluar; rusak, hancur; tercemar kotoran, terganggu.\n
ūhanati: memotong, memancarkan, mengganggu, menghantam, mengeluarkan, berak; menaikkan, mengambil.\n
ūhasati: menertawai, mengejek, mencemoohkan, memeperolok-olokkan, terkikih-kikih, tertawa genit.\n
eka: a.  satu, tunggal, sendirian, masing-masing (_Ye samaṇa-brāhmaṇā ekam attānaṁ damenti_  para pertapa dan brahmana itu menjinakkan diri masing-masing), sama (_ekadivasena_ pada hari yang sama); suatu (_ekadivasaṁ_ suatu hari), sesuatu; **ekaṁ ekaṁ** satu per satu; **eke** sejumlah (_pahūta-jivhe eke kumāre passāmi_  saya melihat sejumlah anak yang berlidah panjang besar); **eko ekāya** seorang pria dan seorang wanita, satu lawan satu; **~uddesa**m. kompak dalam satu Patimokkha, berada dalam satu pelantunan Patimokkha; **~eka** a. satu per satu, masing-masing, setiap; **~pahārena** secara serentak.\n
ekaṁsa: 1. a. berkaitan dengan satu bahu, di atas atau dengan satu bahu (_ekaṁsaṁ uttarāsaṅgaṁ karoti_  menata jubah atas menutupi satu bahu); 2. “satu bagian atau titik”, terfokus, tertentu; penegasan, kepastian, kemutlakan; **ekaṁsena** adv. pasti(nya), secara mutlak, tak terelakkan, selalu demikian.\n
ekagga: a.  tenang, damai, hening; terpusat, menunggal.\n
ekacca: suatu, tertentu, sebagian; **ekacce ** (pl.) sejumlah, beberapa.\n
ekajjhaṁ: adv.  ditempat yang sama, bersama-sama.\n
ekato: adv.  di satu pihak, bersama, berbareng, sekaligus; **~karoti** mengumpulkan; **~ hutvā** “menjadi satu”, bersepakat.\n
ekattha: adv.  di suatu tempat.\n
ekatra: ☞  **ekattha**
ekadā: adv.  sekali, pada suatu kali, sekali waktu, pada waktu bersamaan.\n
ekanta: a.  satu sisi, di satu ekstrem (ujung); terujung; cukup, amat sangat, sekali, sama sekali.\n
ekamantaṁ: di satu sisi, di satu sudut.\n
ekāyana: nt.  langsung, menuju satu arah, mengarah satu tujuan (bukan : satu-satunya jalan).\n
ekāha: adv.  satu hari.\n
ekodi: a.  terfokus, terpusat, terpancang, terarah, menunggal;  **~bhāva**m.  hal atau keadaan terpusat, terkonsentrasi; kemenunggalan.\n
eta(d): ini.\n
etarahi: adv.  sekarang, saat ini, dewasa ini, kini.\n
eti: pergi (ke), mencapai; datang kembali, balik kembali.\n
ettaka: a.  sekian, sebesar ini, sebanyak itu, sebegitu.\n
ettāvata: dengan sebegitu (sebegini).\n
ettha: adv. di sini, di tempat ini, sekarang; dalam hal ini.\n
edhati: makmur, sejahtera, sukses, berkembang.\n
eḷaka: m.  biri-biri (domba) jantan, kambing (bandot liar).\n
eva: (kata penegas)  lah, tuh (_kiṁ evidaṁ_ apa ini), begitu, hanya ….. saja (_aṭṭhikāneva_  hanya (tinggal) tulang saja); nih; betapa; nian; pula, masih; (_naheva_  sungguh tidak); ternyata; _yaññad eva_ (_yaṁ yad eva_)  apa pun; **~rūpa** seperti itu, sedemikian, berwujud seperti itu, cantik, bajik.\n
evaṁ: adv.  demikian(lah), begitu, ya, dengan cara demikian, maka.\n
esa: bentuk m. sg. dari **etad**.\n
esā: bentuk f. sg. dari **etad**.\n
okappeti: meletakkan pikiran pada, mempercayai, meyakini.\n
okassati: menyeret, menarik.\n
okāsa: m.  “penglihatan”, ruang, ruang terbuka, udara, angkasa, ruang udara; penampakan, seperti, tampak; kesempatan, izin, persetujuan; _okāsaṁ karoti  _memberi izin, membolehkan, memberi kesempatan; **sakaraṇ~**yang ada kesempatan untuk melakukannya; **nikkaraṇ~** tak ada kesempatan untuk melakukannya.\n
okirati: menuang, menumpahkan; mencampakkan, membuang.\n
okirinī: a.  terbuang, buangan; bergelimangan (bara api).\n
okilinī: a.  meniris.\n
okkamati: masuk, masuk ke dalam, jatuh ke dalam, tiba pada, mengembangkan, muncul dalam.\n
okkhitta: (pp dari **okkhipati**)  melontar ke bawah, jatuh ke bawah, mengarah ke bawah, tercampak ke bawah, memandang ke bawah.\n
ogāhati (ogāheti): masuk ke dalam, cemplung ke dalam, terjun ke dalam, terserap dalam.\n
ocaraka: m.  penyidik, informan, mata-mata, pengintai.\n
ocarati: mencari, menyelami, menyelidiki, menyidik, mengintip, mengintai.\n
ocita: (pp dari **ocināti**)  dikumpulkan, dipetik, digentas.\n
ocināti (ocinati) :  mengumpulkan, memetik, menggentas; menghina, meremehkan, diabaikan.\n
ojā: f.  kekuatan, sari nutrisi.\n
oṭṭha: m.  1. bibir; 2. unta. [unta ← Skt. oṣṭra]
oḍḍeti: (**uḍḍeti**) melemparkan (jaring), memasang jerat, mengikat, membuang; menunggingkan.\n
oṇirakkha: m.  penjaga benda-benda jaminan atau tanggungan, penjaga barang titipan atau simpanan.\n
otarati: turun, menuruni; kaus.  **otāreti** menyuruh (menyebabkan) turun, membawa turun.\n
otiṇṇa: (pp dari **otarati**)  ke bawah, turun, merosot, tenggelam, hanyut; ditimpa, dipengaruhi, menjadi korban dari, dihampiri, dilanda, ditanggulangi, dikuasai; dilanda atau dikuasai nafsu.\n
ottappa: nt.  takut diasingkan, takut berbuat jahat, segan, sungkan, menyesal. (Vism 464 kāyaduccaritādīhi yeva ottappatī ti ottappaṁ; pāpato ubbegassetaṁ adhivacanaṁ.)
ottharati: menutupi, melindas, menerjang, membentang.\n
odaka: nt.  air; **~antika**tempat di seputar air, tempat dekat air, “berakhir dengan air”, pembilasan akhir, pembilasan dengan air, pembilasan setelah bersenggama, berakhir dengan pembasuhan.\n
odana: m. nt.  nasi.\n
odaniya: a.  nasi, terbuat dari nasi; **~ghara** dapur nasi.\n
odapattakinī: f. a.  istri mangkuk air.\n
odāta: a.  bersih, putih, putih keperakan.\n
onamati: menekuk ke bawah, membungkuk.\n
onamana: nt.  hal menekuk kebawah, membungkuk, merunduk.\n
onītapattapāṇi: m.  setelah memindahkan atau menggeser atau menyingkirkan tangannya dari patta.\n
opakkamika: a.  deraan sakit, serangan mendadak, kejang, akut; cedera.\n
opāta: m.  jatuh, terjun, kejatuhan, turun; lubang perangkap.\n
opuñjāpeti: melumuri, mengolesi, menimbuni, menaburi.\n
opuñjeti: menumpuk,mengonggok, menimbun, membuat suatu onggokan, menutupi dengan; kaus. **puñjāpeti**melumuri, mengolesi.\n
obhata: (pp dari **obharati**)  setelah diambil pergi; dicopot.\n
obhāsa: m.  cahaya, sinar, kirana, binar, kecemerlangan, kegemerlapan, kilauan.\n
obhāsati: 1. bersinar, cemerlang; 2. mencerca, menistakan, melecehkan.\n
omasati: menyentuh, menyenggol (seseorang), menyinggung, mencela, menghina.\n
omasanā: f.  hal menyentuh, meraba turun; sentuhan.\n
omuñcati: melepaskan, mencopot; kaus. **omuṇcāpeti**.\n
oyācati: mengutuk, menyumpahi, menyeranahi, melaknati, menyerapahi.\n
ora: a.  di bawah, rendah, yang buntut, di bagian sini, dunia ini, di dalam; orato  dari sisi ini.\n
orabbhika: m.  penyembelih atau penjagal domba (biri-biri).\n
oramati: berdiam atau berada di sisi ini, berdiri diam, berhenti tidak melanjutkan.\n
oropaṇa: nt.  hal menurunkan, memindahkan, menghilangkan, memangkas (rambut), memelorotkan.\n
oropeti: menurunkan, membawa turun, mencabut, menghilangkan, menyisihkan, membawa pergi, memotong (rambut).\n
orohati: menuruni; kaus. **oropeti**.\n
olaṅghanā: f.  hal menekuk ke bawah, membungkuk.\n
olaṅgheti: membuat loncat turun, membungkuk.\n
olambaka: a.  menggelantung; penyangga, tongkat jalan.\n
olokana: nt.  melihat, memandang, menatap, menginspeksi, meninjau, menilik.\n
ovadati: menasihati, mewejang (memberi wejangan).\n
ovaraka: nt.  kamar (dalam).\n
ovāda: m.  nasihat, wejangan.\n
osarati: mengalir, pergi, berangkat, mendatangi, mengunjungi.\n
osāreti: menyimpan, menaruh, menempatkan, menyisihkan; mengeluarkan, menguraikan, memaparkan, menjelaskan, melakukan rehabilitasi (setelah seseorang bhikkhu telah menjalani penebusan kesalahan).\n
osiñcati: menuangkan, menuangi, memerciki, meletis, menyirami.\n
osīdana: nt.  tenggelam, terjun, turun.\n
ossajjana: nt.  pembebasan, pencampakan, pengeluaran, penanggalan, penyerahan.\n
oharati: mengambil pergi, merenggut, melepaskan; kaus. **ohāreti** menyerahkan, meninggalkan, menanggalkan, melepaskan, memangkas, memotong, mencukur.\n
kakka: nt.  keladak, ampas, endap-endap, sempelah.\n
kakkasa: a.  kasar, keras, kesat. [kasar ← Skt. karkaṡa]
kaṅkhati: 1. meragukan, bingung atas, merasa sangsi; 2. mengharapkan, mengidamkan.\n
kaṅkhā: f.  keraguan, ketidakpastian; pengharapan.\n
kaṅgu: f.  (millet) sekoi (_Panicum italicum_).\n
kacci (kaccid)  : mungkinkah, saya kira, saya pikir mungkin; …., bukan? **kacci te** sungguhkah engkau; **kacci nu kho **mungkinkah, bisa jadi, jangan-jangan, barangkali.\n
kacchapa: m.  kura-kura, penyu.\n
kañcuka: m.  baju (yang ketat membalut badan), korset; lungsungan ular, selumur (kulit ular yang lepas dari tubuh sesudah bertukar kulit); baju baja; baju besi, lemena, baju lamina; ponco; rompi, baju kodok, baju basterop; kelongsong; selubung, selongsong. [kacut ← Skt. kañcuka]
kaññā: f.  gadis, wanita muda.\n
kaṭāha: m. nt.  pot, bejana, jambangan, wadah.\n
kaṭi: m.  pinggul, pinggang; **~suttaka**  nt. ikat pinggang, pelilit pinggul.\n
kaṭikā: f.  persetujuan, kesepakatan; pembicaraan, percakapan.\n
kaṭuka: a. tajam, pedas, perih; pahit, hebat; nt. tajam, menusuk.\n
kaṭula: a.  (PED: mengandung rempah-rempah); bahan bubur; **tekaṭula**tiga bahan bubur yakni _tila_ (wijen), _taṇḍula_ (beras), dan kacang-kacangan (misalnya _mugga_ kacang merah, māsa kacang hijau, _kulattha_ … dan sebagainya). [katul ← Skt. kaṭula]
kaṭṭha: 1. (pp dari **kasati**)  dibajak, digarap; 2. a.  buruk, tak berguna; 3. nt.  potongan kayu, balok, kayu bakar; dahan kayu;  **~hāraka**pengumpul kayu bakar.\n
kaḍḍhana: nt.  hal menarik, menghela; menolak, menampik.\n
kaṭhina: a.  keras, kuat, kokoh; nt. kerangka untuk membuat jubah (bagi para bhikkhu), kain yang dipersembahkan umat kepada bhikkhu untuk membuat jubah tahunan.\n
kaṇājaka: nt.  bubur menir, bubur beras pecah, bubur hancuran beras, bubur yang tercampur dengan sekam.\n
kaṇiṭṭha: a.  yang termuda, bungsu, yang terjunior.\n
kaṇṭaka: nt.  duri, alat yang runcing; tulang; rintangan, gangguan, musuh, pengganggu, pencuri, perampok; **~āpassaya** pembaringan berduri.\n
kaṇṭha: m.  kerongkongan, tenggorokan; leher;  **~suttaka** nt. kalung manik-manik, hiasan kalung.\n
kaṇḍa  (khaṇḍa): m. nt. bagian di antara dua ruas dari suatu batang tanaman; batang, tangkai, gagang panah, panah; bagian (dari suatu buku); bagian kecil, sekelumit atau sepotong; sepenggal waktu, sesaat.\n
kaṇḍuvati (kandūvati): gatal, merasa gatal; menggaruk.\n
kaṇṇa: m.  sudut; telinga; ujung sendok; **kaṇṇe** dengan suara berbisik;  **~chidda**nt.  lubang telinga;  **~suttaka**nt.  benang dari sudut ke sudut; garis kain, untaian hiasan telinga..\n
kaṇṇikā: f.  lempengan/plat (penutup) atap; **kaṇṇika-maṇḍala**m. lempengan bulat (penutup atap).\n
kaṇha: a.  gelap, hitam, berbisa (ular);  f. **kaṇhā** ular.\n
kata: (pp dari **karoti**) telah dilakukan, dibuat, diselesaikan, dipenuhi, dikerjakan; diputuskan. [karta/kerta (Jayakarta, Surakarta Yogyakarta, Kertajaya, Kertasura) ← Skt. kṛta]
katatta: nt.  perbuatan, laku, tindakan.\n
katama: a.  yang mana, apa saja.\n
katara: a.  yang manakah.\n
katādhikāra: a.  yang telah merumuskan sebuah tekad atau niat.\n
kati: berapa (banyak)?
katikā: f.  persetujuan, kontrak, perjanjian, kesepakatan; pembicaraan, perbincangan, percakapan; **~saṇṭhāna**nt. formulir (surat) perjanjian.\n
katipāhan: adv.  (untuk) beberapa hari; **katipāhena**dalam beberapa hari.\n
kattar: m.  pembuat, pelaku, pencipta, pegawa raja, pekerja, utusan raja.\n
kattaradaṇḍa: m.  tongkat (jalan atau petapa).\n
kattha: adv.  di mana, yang mana, ke mana; **~ci(d)**di suatu tempat, di mana pun.\n
katra: ☞  **kattha**
kathaṁ: adv.  bagaimana, mengapa.\n
kathana: nt.  percakapan, pembicaraan, jawaban, wejangan, pendarasan, pelantunan, penuturan, pemaparan.\n
kathā: f.  pembicaraan, perbincangan, percakapan, khotbah, wejangan, ceramah, pidato, pembahasan; kisah, cerita, kata, ucapan, kata-kata, nasihat; penjelasan, pemaparan, diskusi. [kata ← Skt. kathā]
kathika: a.  membicarakan, membabarkan, mengkhotbahkan.\n
katheti: berkata, mengatakan, memberi tahu, menceritakan, mengisahkan, berbicara dengan, bercakap-cakap dengan, melaporkan, membacakan, melantunkan, mendaras, membabarkan, memaparkan, menjelaskan, mengulas, menguraikan, mengkhotbahkan, berbicara tentang, mengacu pada, merujuk pada, menjawab atau memecahkan (persoalan); kaus. **kathāpeti**; pass. **kathīyati**.\n
kadalī: f.  1. pisang raja (_Musa sapientium_); 2. panji (seperti daun pisang); 3. sejenis rusa.\n
kadā: kapan, bilamana; **kadāci**suatu waktu, kadang kala, suatu ketika, mungkin, bisa jadi; **na kadāci**tak pernah.\n
kaddama: m.  lumpur, luluk.\n
kanta: 1. (pp dari **kāmeti**) a. nikmat, menyenangkan, yang disukai, yang dicintai; 2. (pp dari **kantati**) terpotong; dipintal.\n
kantati: 1. memotong; 2. memintal.\n
kantāra: a.  sulit dilalui; gurun, hutan belantara, rimba, jenggala.\n
kandara: m.  1. gua atau ngalau yang umumnya terletak di lereng atau kaki gunung (digunakan sebagai tempat tinggal); 2. lembah kecil, celah-celah gunung, selokan, serokan, _ceruk_, lekuk.\n
kapiñjara (kapiñjala): m.  sejenis burung liar.\n
kappa: a.  disiapkan, diatur; sesuai, layak, pantas; seperti, sebagai, layaknya;  m. peraturan, tata krama, laku; siklus dunia, kalpa, seperentang waktu, kurun waktu; pikiran;  **kappaṁ** adv.  dalam jangka waktu lama atau panjang.\n
kappati: sesuai, pantas, patut, diperkenankan; **kappāpehi**suruhlah orang menyiapkan; **kappāpetu**suruhlah dia menyuruh orang menyiapkan.\n
kappara: m.  siku.\n
kappāsa: m.  kapas, pohon kapas (_Gossypium_). [kapas ← Skt. karpāsa]
kappāsika: a.  dari kapas.\n
kappiya: 1. a.  sesuai peraturan, benar, cocok, layak, pantas, sesuai; nt. yang sesuai, pantas; 2. berkaitan dengan waktu, tunduk terhadap **kappa**, sementara.\n
kappeti: membuat pas, menciptakan, membangun, mendirikan, menyusun, mengatur, menyiapkan, membereskan, memasang, merapikan, membuat, mengadakan, membentuk opini, menerka, berpikir; menakdirkan, menentukan; kaus. **kappāpeti**; pass. **kappiyati**.\n
kabala (kabaḷa): m. nt.  satu suapan makanan (padat atau cair).\n
kabaliṅkāra (kabalīkāra): a.  “yang dibuat dalam suapan bulat”, yang dapat dimakan, makanan materi.\n
kamaṇḍalu: m. nt.  kendi (= **kuṇḍikā**).\n
kamati: berjalan, melangkah, melewati, melintasi, mengarungi, memjelajahi, menapaki, mencapai, sampai, memasuki, berhasil, mempengaruhi, masuk ke dalam, menembusi.\n
kampati: mengguncang, gemetar, bergetar, menggegar, menggeletar, bergoyang, bergoyah.\n
kambala: m. nt.  bahan wol (bulu domba); laken (sekelat; kain wol; kain tenun dari bulu domba); selimut atau pakaian wol, selimut kambeli (kain selubung dari bulu domba); selimut atau kain selubung; bahan rajutan bulu; benang wol. [kambeli ← Skt. kambala]
kamma: nt.  perbuatan, tindakan, yang dilakukan, usaha, kegiatan, pekerjaan, profesi; persidangan (rapat) Sanggha; proses persidangan Sanggha; niat (_cetanā_; AN 6:63; A 3:415; A 5:292); _kammaṁ karoti  _menyidangkan; **~pathā**modus perbuatan; **~vācā**f. resolusi; **~vācāriya**m.  pimpinan rapat Sanggha. (_Cetanāhaṁ bhikkhave kammaṁ vadāmi cetayitvā kammaṁ karoti kāyena vācāya manasā_ A. 3:415) [karma ← Skt. karma]
kammanīya (kammaṇiya, kammañña): a. ‘yang dapat bekerja’, terampil, lincah, gesit, cekatan; lentur.\n
kammanta: m.  perbuatan, tindakan, pekerjaan, pengerjaan, urusan.\n
kara: a.  membuat, menghasilkan, membentuk, melakukan, mengerjakan;  m.  tangan (“yang membuat”).\n
karaṇa: a.  melakukan, membuat, menyebabkan, menimbulkan, menghasilkan;  nt.  pembuatan, penghasilan, pelaksanaan, hal melakukan; penyiapan; keadaan, kondisi.\n
karaṇīya: a.  yang seyogianya dilakukan, dikerjakan; nt. tugas, kewajiban, urusan.\n
karamara: “yang seharusnya mati di tangan (musuh)” namun dibiarkan hidup untuk dijadikan budak; budak (tawanan perang); **~ānītā** budak wanita (tawanan perang) yang kemudian dijadikan sebagai istri.\n
karaḷa (karala): m.  utas, gumpal, jurai, jumbai.\n
karin: a.  ‘yang mempunyai tangan’; gajah.\n
karuṇā: f.  belas kasih, kasih sayang. (Sn.A. _ahita-dukkhā-panaya-kāmatā _: keinginan untuk mengenyahkan kemudaratan dan penderitaan pihak lain; atau Vism 318 _paradukkhe sati sādhūnaṁ  hadayakampanaṁ  karoti_)
karoti: melakukan, bertindak, membuat, berbuat, membangun, mengerjakan, mendirikan, menyelenggarakan, melangsungkan, mengadakan, mewujudkan, menghasilkan, mengenakan; menulis; menyusun; mengenakan (busana, hukuman);  mengubah menjadi, menggunakan sebagai, menjadikan, menempatkan; menetapkan, memutuskan; **kārāpesi**ia (waktu itu) menyuruh orang membangun; **kāressati**ia akan menyuruh orang membuat, ia akan memerintah; **kāriyati**ia disuruh membuat; **kārento** (=**kārayato**) (tatkala ia) menyuruh orang membuat; **kārita**sudah menyuruh orang membuat, disuruh membuat; **kārāpita**sudah menyuruh orang membangun, disuruh membangun; **kārāpetvā** setelah menyuruh orang membangun; pass. **karīyati**.\n
karoto: bentuk genitif atau datif dari “present participle” (**karonto**) kata kerja **karoti**.\n
kalaha: m.  pertengkaran, percekcokan, perseteruan, perselisihan.\n
kalyāṇa: a.  baik, bagus, bajik, menawan hati (_mālā kalyāṇā_) nt.  kebajikan, kebaikan, kesejahteraan; **~dhamma**a.  penuh kebajikan; m. kebajikan.\n
kavandha: m. nt.  badan (tanpa kepala), togok; katai (cebol) tak berkepala (karena kepalanya telah dijebloskan ke dalam badan).\n
kavāṭa: m. nt.  daun pintu; tiang pintu; jendela; _kavāṭaṁ paṇāmeti _ membuka pintu; _kavāṭaṁ ākoṭeti  _mengetuk pintu.\n
kavi: m.  penyair, sastrawan, penulis sajak; (Dalam A. 2:230 dan DA. 1:95 disebutkan ada empat jenis : _cintā_, _suta_, _attha_, _paṭibhāṇa_).\n
kasaṭa: a.  buruk, najis, pahit, sengit (tajam), memuakkan, menjijikkan; hambar, tawar, cabar, boyak; m. cacat, kesalahan, noda; remah(-remah), repih-repih (sisa-sisa makanan dsb yang ketinggalan di tempat makan); serpihan; ampas, sampah; sesuatu yang pahit atau berasa tajam; jus pahit.\n
kasā: f.  cemeti, cambuk, pecut.\n
kasmā: mengapa, karena apa.\n
kassaka: m. petani, peladang, pecocok tanam.\n
kahaṁ: di mana, ke mana.\n
kahāpana: m.  koin tembaga persegi, uang logam; uang; hadiah atau imbalan uang.\n
kāka: m.  burung gagak.\n
kākī: f.  burung gagak betina.\n
kāma: m. kesenangan; nafsu, kenikmatan, kesenangan indriawi; kesukaan, kegandrungan (_yathā kāmaṁ_ sesuka hati, manasuka); ~guṇa  m.  (faktor atau kualitas) kesenangan indriawi; ~bhoga m. hal menikmati kesenangan indriawi; kāmesu kāmasukhallika kegandrungan dan suka cita terhadap kesenangan indriawi; vatthu~ objek indriawi; kilesa~ nafsu kotoran batin. [kama ← Skt. kāma]
kāya: m.  onggokan, kumpulan, badan, jasmani (mencakup pula tindak-tanduk darinya), batang tubuh, sosok, kelompok; ( = deha, sarīra, nikāya); **~daḷhībahula**a.  gemar mengekarkan tubuh.\n
kāyika: a.  milik tubuh, jasmani, berhubungan dengan tubuh; termasuk dalam kelompok atau rombongan, pengikut, pengiring, kawanan.\n
kāra: m.  perbuatan, laku, tindakan, pelaksanaan, perilaku; pelaku; pembuatan, pembentukan, keadaan, penerapan, perlakuan; huruf, suku kata, fonem; pembuat, pekerja.\n
kāraka: m.  pelaku, pelaksana, pembuat, pengabdi; **kattu~** kalimat bentuk aktif; **kamma~** kalimat bentuk pasif.\n
kāraṇa: nt.  perbuatan, tindakan, pekerjaan, tugas, kewajiban (_kāraṇaṁ kārāpeti_ ia menyuruh seseorang melakukan (suatu) pekerjaan; _kiṁ kāraṇaṁ ajja kāressati  _pekerjaan apa yang akan dia tugaskan hari ini?); alasan, sebab;  **kāraṇā** (abl.) dengan, melalui; **kāraṇaṭṭhā**  demi, untuk, dengan tujuan, dengan pamrih; **nikkāraṇā**tanpa pamrih. [karena ← Skt. kāraṇa]
kāraṇika: m.  pembuat, pembuat panah; pemanah, eksekutor.\n
kārī: m. pelaku, pelaksana.\n
kāruñña: nt.  belas kasih, kasihan. [karunia ← Skt. kāruṇya]
kāla: m. waktu; kālaṁ karoti  meninggal, menemui ajal; kālena kālaṁ  dari waktu ke waktu, secara teratur, secara berkala (periodik), terus menerus; ~kaṇṇī  m. yang bertelinga hitam, orang sial. [kala ← Skt. kāla]
kāḷa: m.  gelap, hitam; **~kaṇṇī**bertelinga hitam, sial, tak beruntung.\n
kāḷaka: a.  hitam, bernoda;  nt. noda hitam; noda; butiran hitam dalam beras; _apagatakāḷaka_ tanpa cacat atau noda.\n
kāsāya (kāsāva): a.  kuning; jubah berpewarna, jubah kekuning-kuningan para bhikkhu.\n
kāsika: a.  yang berasal atau berhubungan dengan negeri Kāsī atau Benares.\n
kāsu: m.  lubang; **aṅgāra~**lubang api.\n
kiṁ: apa? **kiṁ tava patthanāya** untuk apa pengharapan (doa) Anda? **kiṁ idaṁ** inilah, inilah sebabnya, oleh sebab itu; **kiṁ sūdha vittaṁ purisassa seṭṭhaṁ** kalau begitu apa harta manusia yang terbaik di dunia ini? **kiṁ nu kho** mengapa? apakah? **kissa hetu** apa sebabnya? **kiṁ kahāsi** apa yang akan Anda lakukan? (Anda akan melakukan apa?) **kiṁ āgamma kiṁ ārabbha** apa dasarnya apa alasannya? **kiṁ nissita** apa tujuannya? **kismiṁ vivādo **pertengkaran dalam hal apa? **kimhi sikkhamāno **dilatih dalam hal apa? **kiṁ idāni pi dinne te labheyyuṁ** apakah mereka akan menerima apa yang diberikan sekarang? **kiṁ imasmiṁ attabhāve pitaraṁ pucchasi udāhu atīte**? apakah Anda menanyakan ayah Anda dalam kelahiran ini atau kelahiran lampau? **kiñcāpi** walaupun; **kiṁ nakkhattaṁ kīḷissasi udāhu bhatiṁ karissasi** apakah Anda mau berlibur atau bekerja? **kimo nu** lantas mengapa? **kiṁ pana** apalagi; **kiṁ pana bhante addasa **tidakkah Bhante melihat? **kiṁ pana tvaṁ maññasi** tidakkah Anda berpikir demikian? **kin ti** bagaimana? **kin ti te sutaṁ** tidakkah Anda dengar? **kiñ cāpi te tattha yatā caranti** betapa pun mereka berupaya di sana.\n
kiṅkiṇika: m. nt.  lonceng kecil, giring-giring, kelinting(an).\n
kicca: a.  yang harus dilakukan atau dikerjakan; nt. sesuatu yang dilakukan; tugas, kewajiban, urusan, kesibukan, perhatian, pelayanan, upacara, pelaksanaan, perbuatan, pekerjaan atau fungsi, peran, aktivitas.\n
kiñci: apa pun, suatu.\n
kiñcikkha: nt.  sepele, urusan kecil.\n
kiṇāti: membeli.\n
kita: (pp dari **kṛ**)  dihiasi, dilumuri, dikotori, bergelimang.\n
kitava (kitavā): m.  penipu; a. dengan menipu.\n
kittaka: seberapa besar, seberapa banyak; sedikit.\n
kitti: f.  kemasyhuran, reputasi, nama baik, kegemilangan; ~sadda  m. reputasi, nama harum.\n
kipillikā: f.  (**kipillaka** nt.) semut.\n
kibbisa: nt.  kesalahan, kekhilafan, kekeliruan, kekurangan, cela, dosa; kejahatan, kekejaman, kekerasan.\n
kira (kila): adv.  sungguh, betul; sekarang, lantas, Anda tahu, konon, katanya, kiranya, sebagaimana diceritakan.\n
kiriyā (kriyā): f.  tindakan, perbuatan, kinerja; **~vibhatti**f.  konjugasi kata kerja.\n
kilañjā: f.  tikar, kerai, bidai, sekat; berkas kayu, peti kayu.\n
kilanta: (pp dari **kilamati**)  lelah, capai, lesu.\n
kilamati: kekurangan; lelah, letih, capai, berada dalam kesulitan atau kesengsaraan.\n
kilamatha: m.  kelelahan, keletihan, kepenatan, kepayahan, hal menyengsarakan, menyiksa.\n
kilameti: lelah, menyengsarakan.\n
kilāsu: m.  terkuras habis, lelah, lesu, pasif; **akilāsu** aktif tanpa kenal lelah.\n
kilijjati: menjadi panas, meradang, menjadi radang, bernanah.\n
kiliṭṭha: (pp dari **kilissati**) bernoda, tercemar, terkotori, kotor, tidak bersih, bobrok, bejat, penuh nafsu.\n
kilinna: (pp dari **kilijjati**)  basah (oleh ludah, peluh dsb), bercucuran, menjadi radang, meradang.\n
kilesa: m.  kotoran (batin); noda (batin); nafsu; bejat moral.\n
kisa: a.  kurus, ceking, kurus kering, kurus mering, kerempeng (sangat kurus sehingga tulang rusuk tampak menonjol).\n
kīta: (pp dari **kiṇāti**)  dibeli.\n
kīdisa: seperti apa, macam apa, yang bagaimanakah, yang manakah.\n
kīḷati: bermain, menghibur diri, berhibur.\n
kīḷā: f.  permainan, olahraga, hiburan; **nakkhatta-kīḷaṁ kīḷati** merayakan suatu festival (saat bulan purnama sedang berada dalam suatu gugus bintang tertentu).\n
kīḷita: (pp dari **kīḷati**) bermain, dirayakan.\n
kīvant (kīva): berapa besar? berapa banyak? bagaimana? seberapa?
kukkucca: m.  perbuatan buruk (jahat), perilaku bobrok; sesal, penyesalan, perasaan bersalah, kecemasan, kekhawatiran.\n
kukkuccaka: a.  cermat, berhati-hati.\n
kukkuccāyati: merasa menyesal, menyesali, cemas, kuatir.\n
kukkuṭa: m. ayam jantan.\n
kukkuṭī: f.  ayam betina.\n
kukkura: m.  anjing, anjing pemburu.\n
kucchi: m.  rongga, perut atau rahim; bagian dalam, internal. [koci ← Skt. kukṣi]
kujjhati: marah terhadap (dat.).\n
kuṭaja: m.  sejenis akar-akaran (_Wrightia antidysenterica_ atau _Nericum antidysentericum_).\n
kuṭikā: f.  pondok atau gubuk kecil (biasanya terbuat dari tangkai pohon, rumput dan lempung); kuti, bilik kediaman bhikkhu.\n
kuṭī: f.  kediaman berkamar tunggal, pondok, gubuk, kamar, bilik, ruang, pernaungan.\n
kuṭumba: nt.  harta milik keluarga; _kuṭumbaṁ saṇṭhapeti  _membangun usaha, mendirikan perusahaan.\n
kuṭṭha: nt.  1. penyakit kusta; 2. sejenis tanaman wewangian atau rempah-rempah (_Costus speciosus_). [kusta ← Skt. kuṣṭhā]
kuṭhāri: f.  kapak, beliung.\n
kuḍḍa: m.  dinding yang terbuat dari bilah-bilah berlapis tanah, bidai berlapis tanah, pagar jaro berlapis tanah; dinding kajang berlapis tanah; dinding, ada tiga macam: dari batu bata, batu dan kayu (Vin.).\n
kuṇa: a.  bengkok, melengkung, pincang.\n
kuṇapa: m.  mayat, bangkai, jenazah.\n
kuṇī: nt.  yang bertangan bengkok.\n
kuṇḍikā: f.  kendi.\n
kuto: dari mana; mengapa.\n
kuttaka: nt.  karpet (permadani) wol;  a. “rekayasa”, dibuat-buat, pura-pura, palsu.\n
kuthati: memasak, mendidihkan, merebus.\n
kuthita: (pp dari **kuthati**)  dididihkan, dimasak; dicerna; disiksa.\n
kudassu: (kata seru)  pasti, tentu saja, sungguh, niscaya.\n
kuddāla: m.  sekop, cangkul, pacul.\n
kuddha: a.  marah.\n
kupita: (pp dari **kuppati**)  diguncang, diganggu, terusik, marah.\n
kumāra: m.  remaja, bocah, putra.\n
kumāraka: m.  bocah, remaja, pemuda; nt.  hal-hal yang berbau kekanak-kanakan.\n
kumārī: f.  gadis, perawan.\n
kumina: nt.  jala ikan, jaring ikan; _bubu, lukah_.\n
kumbha: m.  belanga, buyung, kumba, tempayan, pasu, jambangan, kendi, buli-buli, guli; bonggol (ponok) pada dahi gajah; **~kāra**pembuat (barang-barang) tembikar; kundi (pengrajin barang yang terbuat dari tanah liat). [kumba ← Skt. kumbha]
kumbhaṇḍa: m.  sejenis peri atau jin yang sekelompok dengan yakkha, rakkhasa (raksasa) dan asura; jin berbuah pelir besar (seperti kumba); sejenis labu (_pumpkin_, labu merah?).\n
kumbhimukha: nt.  bibir tong atau pasu, mulut bejana atau belanga.\n
kumbhī: f.  tong besar, bejana atau jambangan besar, pasu.\n
kummāsa: m.  bubur barli; terdiri dari campuran tepung, rempah-rempah, dsb.\n
kula: nt.  keluarga (umat), kaum; perumah tangga; **~putta** m. putra berbudi, putra keluarga terpandang. [keluarga ← Skt. kulavarga]
kulattha: m.  sejenis _vetch_ (ye wan dou); miju-miju (_lentil_).\n
kulala: m.  burung hering (_Gyps indicus nudiceps_), _burung elang_, falkon (_Falconidae_).\n
kulāvaka: nt.  sarang.\n
kulūpaka: a.  yang kerap mengunjungi keluarga (umat).\n
kusa: m.  rumput kusa (PED: _Poa cynosuroides_; KBBI: _Echionochloa colona_); sehelai rumput yang dipakai sebagai tanda atau alat undian; **~cīra** rajutan rumput kusa. [kusa ← Skt. kuṡa]
kusala: a. pandai, tangkas, terampil, ahli, baik, benar, bajik; nt. kebaikan, kebajikan, perbuatan bajik.\n
kuhiṁ: adv.  di mana?
kūjati: berkicau.\n
kūjavāra: m.  Hari Selasa.\n
kūṭa: 1. a.  salah, keliru, palsu, menipu, membohongi;  nt. perangkap, jerat; kesalahan, kekeliruan, kebohongan, penipuan; 2. m. nt.  tonjolan, jendul, puncak; atap, puncak suatu rumah, bubungan; pucuk; onggokan; timbunan; titik tertinggi; 3. nt. palu; 4. a.  tanpa tanduk, tidak bertanduk, dogol, dongkol; **~āgāra**nt. bangunan beratap runcing, bangunan bermenara, bangunan bertingkat.\n
kūpa: m.  lubang, rongga; tiang (kapal).\n
kūla: nt. lereng, tepian, pematang atau tanggul (penahan air sungai).\n
kevala: a.  hanya, sendirian; seluruh, semua _(~paripuṇṇa  _utuh menyeluruh, lengkap mencakup semuanya); namun;**kevalaṁ **adv. hanya (_na kevalañ ca viriyam eva sati pi me ārammaṇābhi-mukhībhāvena upaṭṭhitā ahosi_)
kesa: m.  rambut.\n
koka: m.  1. _serigala_, anjing hutan (_Canis rutilans_); 2. sejenis pohon (_Phoenix sylvestris_).\n
koccha: nt.  bangku tak bersandaran, kursi rotan; sisir.\n
koñca: m.  bangau; raungan gajah.\n
koṭi: f.  penghabisan, akhir; ujung, puncak, titik; masa (**pubba~** masa silam; **purima~** atau **pacchima~** masa mendatang); bilangan besar, biasanya merujuk ke angka sepuluh juta, kadang-kadang seratus ribu (keti). [keti ← Skt. koṭi]
koṭṭana: m.  penggerusan, penghancuran, penumbukan; penebasan.\n
koṭṭeti: memukul, menghantam, meremukkan, menghancurkan, menumbuk; meratakan (lantai); memotong, membunuh.\n
koṭṭha:  1.  m. nt.  ruang, kamar, bilik; perut; kamar kecil, kamar bhikkhu, kamar gudang; sarung (parang); 2. m. sejenis burung; 3. m. sejenis tanaman (_Costus speciosus_?).\n
koṭṭhaka: 1. nt. “sejenis _koṭṭha_”, benteng di atas pintu gerbang yang digunakan sebagai ruang penyimpan berbagai barang, gudang, lumbung, perbendaharaan, kamar, ruang penyimpan air; gudang, perbendaharaan, kamar (**udaka~** kamar mandi; **nahāna~** kamar mandi; **piṭṭhi~** kamar belakang), ruang, bilik; 2. m. _paddy-bird_.\n
koṭṭhāsa: m.  bagian, bilik, porsi.\n
kotthalī (koṭṭhalī): karung (?), kantung.\n
kopa: m.  kemarahan, dendam.\n
kopīna: nt.  kemaluan, yang memalukan; cawat, kain pinggang.\n
kovida: m.  orang yang unggul memiliki kebijaksanaan (dalam hal _Dhamma_, _magga_, atau _ariyasacca_) [Mirip dengan _medhāvin_ dan _paṇḍita_.]
kosa: m.  ruang yang berisikan sesuatu; ruang penyimpanan, gudang; tempat penyimpanan harta benda, lumbung, sarung atau selongsong, kepompong, kulit pembalut penis; bagian dalam. [kosa ← Skt. koṡa]
kosajja: .  nt.  kelambanan, ketidakcekatan, kelesuan, kemalasan.\n
khaṇa: m.  ketika, saat, momen.\n
khaṇati: menggali, menumbangkan, menghancurkan.\n
khaṇika: a.  tak stabil, sementara, sejenak.\n
khaṇḍa: a.  patah, pecah, hancur, compeng, compes, cuil, gempil, rempak, rompeng, rompes, serpih, sumbing, cacat;  m. nt. pas (jalan pintas sempit di daerah pegunungan); pecahan, potongan, cuil, serpih; camilan; **~ākhaṇḍika**potong demi potong, pecahan belaka, hancur berkeping-keping.\n
khattiya: m.  orang keturunan kaum Arya, orang yang berkasta kesatria (Status sosialnya tertinggi, selalu disebut paling awal. Semua raja atau kepala suku masuk dalam golongan ini.) [kesatria ← Skt. kṣatriya]
khanti (khantī): f.  kesabaran, ketabahan, perkenan.\n
khandha: m.  sosok tubuh, terutama bagian punggung; pundak, punggung; batang tubuh; batang pohon; bagian, bab; kumpulan, pumpunan, gugus(an); massa; semua bagian-bagian dari; faktor atau unsur pembentuk; agregat, kelompok (kehidupan).\n
khama: a.  sabar, siap memaafkan, menerima, menurut, mengeras, membeku, bertahan, tahan terhadap, cocok untuk, tabah (_akkosantaṁ na paccakosati_), toleran.\n
khamati: bersabar, menerima, tabah, memaafkan; sesuai, tampak baik, berkenan (_yathā te khameyya tathā taṁ byākareyyāsi_ jawablah bila Anda berkenan); grd. **khamanīya** menjadi reda, menjadi sembuh (dari suatu penyakit); kaus. **khamāpeti**menenangkan, minta maaf.\n
khamana: nt.  hal bersabar atau tabah menahan penderitaan.\n
khamā: f.  kesabaran, ketabahan, toleransi; bumi.\n
khaya: m.  habis, lebur, enyah, lenyap, berakhir.\n
khayita: a.  membusuk, rusak.\n
khara: a.  kasar, keras, kaku, tajam, sakit; acak-acakan; m. keledai; gergaji.\n
khalika (khalikā f.): m.  papan dadu; _khalikāya kīḷati_  bermain dadu.\n
khalu: sungguh, betul, begitulah.\n
khallāṭiya: nt.  gundul, botak, plontos.\n
khādati: mengunyah, menggigit, makan, menelan, menghancurkan, menyantap, menikmati.\n
khādaniya: m.  makanan pendamping/ sekunder/ sampingan/ pelengkap/  tambahan, makanan ringan, makanan keras.\n
khāyita: = **khādita** (pp dari **khādati**)
khāra: m.  soda, senyawa alkalin/kaustik; a.  basa, alkalin; **~udaka**nt.  air kaustik.\n
khiḍḍā: m.  permainan, hiburan, kesenangan. [krida ← Skt. krīḍā]
khitta: (pp dari **khipati**)  dilemparkan, dibuang, dicampakkan;  **~citta**nt.  pikiran yang kacau, bingung, gusar, kalut, kalap, hilang pikiran.\n
khippa: a.  cepat; sejenis jaring ikan atau keranjang belut;  **khippaṁ**adv. secara cepat, bergegas.\n
khila: m. nt.  tanah tandus, atau gersang; batin yang gersang; kila (pancang); **~jāta** geregetan.\n
khīṇa: (pp dari **khīyati**) habis, tandas, berakhir, hancur, enyah, lenyap, terkikis habis, tanpa.\n
khīyati: (pass. dari **khayati**) terkuras habis, habis, tandas, tanggal dari, menjadi sedih atau tertekan; mencela, mengkritik; menggerutu. (_Tassa avaṇṇaṁ kathenti pakāsenti_)
khīra: nt.  susu, cairan seperti susu.\n
khīla: m.  tonggak, tiang, pancang, patokan, baut, pasak, kila. [kila ← Skt. kīla]
khuṁseti: mencaci-maki, memarahi, mengutuk, menyumpahi, menyerapahi, menyeranah.\n
khudda: a.  kecil, rendah; sedikit, sepele; campuran.\n
khuddaka: =**khudda**
khubhati (saṁkhubhati) :  mengguncang, mengaduk.\n
khetta: nt.  ladang, sawah, sebidang tanah, lokasi, domain, lahan, lapangan, padang, tapak (lahan tempat tumbuh tanaman hutan). [setra ← Skt. kṣetra]
khema: a.  penuh dengan kedamaian, aman, tenteram;  nt. tempat yang damai, aman, tenteram; pernaungan.\n
kho: (bentuk pendek dari **khalu**) [avadhārana : kata penekan, penegas] sungguh, betul, lah, begitulah, sekarang, lantas, kah; sebaliknya, tetapi.\n
khobha: m.  guncang.\n
gaccha: m.  semak-semak, belukar, terna.\n
gacchati: pergi, bergerak, berpindah, berjalan, menuju, tiba pada, menjadi tahu, mengalami, menyadari, akhirnya menjadi.\n
gaṇa: m.  kelompok, kumpulan, gerombolan, himpunan, pumpunan; kelompok bhikkhu yang terdiri dari dua atau tiga orang.\n
gaṇaka: m.  penghitung, penilai, penaksir, akuntan, pengawas, penjaga.\n
gaṇakī: f.  pelacur; istri peramal.\n
gaṇanā: f. perhitungan, aritmatika, angka; penghitungan, sensus, statistik; ilmu berhitung, ilmu aritmatika; **~patha** m. perhitungan waktu, jangka waktu.\n
gaṇikā: f. 1. = **gaṇakī** “milik orang banyak”; pelacur; 2. = **gaṇanā**
gaṇeti: menghitung, membilang, menjumlahkan; memperhitungkan, mempertimbangkan, menganggap, memperhatikan; **gaṇīyati**.\n
gaṇhati (gaṇhāti)  : mengambil, menggenggam, memegang, mencengkeram, menangkap, mengulum, menguasai, menggunakan (mantra), mencaplok, menyebutkan satu per satu; **gahetvā** dengan (_tidaṇḍaṁ gahetvā caranto  satta bhikkhū gahetvā agamāsi_).\n
gata: (pp dari **gacchati**) yang telah pergi, lewat, tiba pada, mencapai (tujuan); yang telah masuk dalam, yang berhubungan dengan; bernuansa, berperilaku (_kāyagata_ sepak terjang jasmani), bergaya, menapaki, menempuh, bernasib, dalam keadaan (_ye hi abhāvaṅgatā te puna kathaṁ uppajjissanti_).\n
gati: f.  tempuhan, hal pergi, arah, jalan, hal meninggal; alam kehidupan yang dituju setelah meninggal, alam kelahiran; nasib kelahiran (berikut), alam penjelajahan; alam penuh siksaan.\n
gatta: nt.  badan; **gattāni** (pl.) kaki dan tangan. [gatra ← Skt. gātra]
gadrabha: m.  keledai.\n
gantha: m.  ikatan, belenggu, kungkungan, belitan; komposisi, karya tulis, naskah, buku, kitab.\n
ganthati (gantheti): mengikat, membebat, menjalin, menyusun, menggubah.\n
gandha: m.  bau, aroma, parfum, wewangian. [ganda ← Skt. gandha]
gandhabba: m.  musisi, penyanyi; musisi surgawi di bawah kendali _Dhataraṭṭha_ sebagai pelayan para dewa, masih terikat pada kesenangan indriawi; bakal makhluk hidup (yang harus hadir agar bisa terjadi kehamilan M. 38). [gandarwa /genderuwo ← Skt. gandharva]
gandhabbā: f.  musik, nyanyian, lagu.\n
gabbha: m. rongga, ruang; rahim, peranakan (= **mātukucchi**); kandungan, janin (=_gabbhe nibbattanaka-satta_), embryo, fetus; **~pātana** nt. pengguguran kandungan, aborsi, ramuan penggugur kandungan; **~seyyā** terbaring dalam rahim, dikandung. [garba ← Skt. garbha]
gabbhinī: f. a.  hamil, mengandung.\n
gama: a.  pergi, sanggup pergi, menuju, berjalan;  m.  jalan, kepergian ke, pulang.\n
gamana: a.  mengarah pada, menuju;  nt. hal pergi, berjalan, bergerak, menempuh, menuju, mengarah pada, menapaki jalan, pergi menuju; lintas(an).\n
gambhīra: a.  dalam, tak terkirakan, sahih, sukar; nt. kedalaman, hal sangat mendalam, landasan nan dalam (landasan yang kokoh); **~sita** terletak amat dalam; sahih.\n
gamma: a.  yang bersifat seperti orang kampung, awam, kasar, tak tahu adat, kampungan, _tidak beradab_.\n
garahati: mengecam, menyalahkan, mencerca, mencela.\n
garahā: f.  kecaman, celaan, omelan.\n
garahin: a.  mencela, mengecam.\n
garu: a.  berat; penting, bermartabat, dihormati, dihargai, bernilai, mengikuti, menghormati, memuliakan, mengindahkan.\n
garuka: a.  agak berat; berat, serius, gawat, penting, mulia, patut dihormati, “berat pada”, condong (pada), gemar, menganggap penting, menghormati.\n
garukata: (pp dari **garukaroti**)  dihormati.\n
garukaroti: menghormati, menjunjung, memuliakan.\n
garuḷa: m.  nama sejenis burung gaib (raksasa) yang senantiasa bertarung dengan naga. Dalam legenda India, Wisnu mengendarai burung garuda. [garuda ← Skt. garuḍa]
gaḷagalāyati: bergemuruh.\n
gaha: m.  rumah, panti; **~kūṭa**m. nt. balok nok (ridge-pole); **~ṭṭha**m. perumah tangga; **~pati** m. pemilik rumah, kepala rumah tangga. [gerha ← Skt. gṛha]
gahaṇa: a.  _memegang_, menggenggam, mengambil, menangkap, memperoleh, panen.\n
gāthā: f.  syair, bait, baris, larik; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**).\n
gāma: m.  permukiman, dusun kecil; suatu wilayah atau kampung yang memiliki perbatasan dan berbeda dari lingkungan sekitarnya; kampung, desa, dusun, udik; **~kūṭa** nt. penipu, penjilat, peleceh.\n
gāmaka: m.  perkampungan, dusun, desa; penduduk desa.\n
gāmanta: m.  seputar kampung, pinggiran dusun, perkampungan.\n
gāmika: m.  penduduk desa; penguasa desa, pengawas wilayah;  a.  pergi berkelana, bepergian.\n
gāmin: ( f. **gāmiṇī**) a. berjalan, menapaki, menuju.\n
gāyati: bernyanyi, mengumandangkan, berdendang, melantunkan.\n
gārayha: (grd. **garahati**)  a.  rendah, hina, terkutuk, dicela.\n
gārava: m. nt.  penghormatan, penghargaan, respek, takzim.\n
gāvī: f.  sapi, lembu.\n
gāha: m. hal menangkap, mencengkeram, menggenggam, memegang, mengambil.\n
gāhin: a.  memegang, mengambil, berupaya.\n
gijjha: m.  burung hering, burung nasar (_Gyps indicus nudiceps_), burung pemakan bangkai;  a.  serakah, haus akan.\n
gimha: m.  panas, musim panas, musim kemarau.\n
gilati: menelan; kaus. **gilāpeti** membuat menelan.\n
gilāna: a.  sakit; **~paccayabhesajja** obat penyembuh sakit, obat-obatan. [gila/gulana ← Skt. glāna]
gilānālaya: m. nt.  pura-pura sakit.\n
giri: m.  gunung, giri. [giri ← Skt. giri]
gihin: a.  berumah tangga.\n
gīvā: f.  leher.\n
guṇa: m.  1. benang, tali, senar; unsur, bahan, komponen, faktor, bagian; kualitas, sifat, kualitas bagus, keuntungan, kebajikan; 2. bola, gumpalan, rangkaian, untaian; 3. ulat kayu. [guna ← Skt. guṇa]
gutti: f.  perlindungan, pertahanan, penjagaan, pengawalan; kesiagaan.\n
gumba: m. pasukan, gerombolan, gundukan, pumpunan, kawanan; belukar, semak-semak, rimba, sarang, jerumun. [gulma ← Skt. gulma]
guru: a.  yang terhormat, yang mulia, guru; **~vāra**m.  Hari Kamis. [guru ← Skt. guru]
guḷa: m.  1. bola; 2. gula; 3. gerombol, kumpulan. [gula/guli ← Skt. guḷa]
guḷā: f.  bengkak, bincul, benjolan, bintil, bintul, bisul.\n
guhā: f.  tempat persembunyian, gua; (menurut Buddhaghosa)  pernaungan yang terbuat dari batu bata, batu (karang), kayu atau tanah; bungker. [gua ← Skt. guhā]
gūtha: m.  kotoran, tahi, berak, tinja, feses; **~kūpa** m. kakus, jamban, tandas, peturasan, tempat buang air.\n
geyya: nt.  ragam kitab suci yang terdiri dari campuran prosa dan syair; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**).\n
geruka: nt. f.  oker kuning, kapur merah.\n
geha: nt.  kediaman, pondok, rumah, panti, rumah tangga. [gerha ← Skt. gṛha]
go: m. f.  lembu, sapi; (pl.) ternak; **~maya**m. nt  kotoran sapi; **~vikattana** nt. pisau penjagal sapi.\n
gocara: m.  ‘padang rumput penggembalaan”, tanah penggembalaan sapi; wilayah penjelajahan, lingkup kegiatan; hal mencari makanan; makanan ternak; makanan;  a.  bergantung pada, hidup bersandar pada; bersekutu dengan;  m. nt.  medan, ruang lingkup, objek (indra),
goṇa: m.  banteng, lembu atau sapi jantan.\n
gotama: marga atau nama keluarga (_gotta_) Sang Buddha sebelum meninggalkan kehidupan berumah tangga.\n
gotta: nt.  wangsa, silsilah keturunan, marga, suku, kaum.\n
godhā: f. 1. iguana, sejenis kadal berbadan besar; 2. senar (dawai) kecapi.\n
godhūma: m.  gandum (_Triticum aestivum_). [gandum ← Skt. godhūma]
gopānasī: f.  kasau, yang melengkung.\n
gopālaka: m.  penggembala sapi.\n
gopālikā: f.  wanita penggembal sapi.\n
gopita: (pp dari **gopeti**)  dilindungi, dijaga, diawasi, dirawat.\n
gopeti: mengawasi, melindungi, menjaga.\n
gomaya: nt.  kotoran sapi.\n
golikā: f. sejenis kadal atau cecak.\n
goḷaka: m.  bola, onde-onde.\n
ghaṁsati: 1. menggosok, meremukkan, melumatkan, menghancurkan, menggerus, menggilas, melindas; 2. merasa senang atau puas, gembira.\n
ghaṁsana: m.  pengusapan, pengelapan.\n
ghaṭa: 1. m. bejana berongga, mangkuk, jambangan, kendi, buyung, bocong; 2. m. f. kumpulan, onggokan, gumpalan, massa, pampat, padatan, tumpat.\n
ghaṭikā: f.  1. mangkuk kecil untuk meminta-minta; 2. tongkat kecil, ranting; permainan gatrik _(tip-cat” sticks_, memukul sebuah tongkat kecil dengan sebuah tongkat yang lebih panjang); longgokan ranting; (tangkai) gerendel.\n
ghaṭṭeti: memukul, menghantam, mengetok, membenturkan, menyenggol, menyentuh, menggesek, menggosok, mengurut, menggarap; menyerang, memperolok-olokkan, menolak, menampik.\n
ghana: 1. a. padat (berisi), tebal; m. janin pada tahap terakhir (keempat) sebelum lahir (dari tahap-tahapan berikut _kalala_, _abbuda_, _pesī_, _ghana_); 2. tongkat, gada, palu.\n
ghara: nt.  rumah, bilik; **~āvāsa** kehidupan berumah tangga; **~bandhana** nt. ikatan rumah tangga; hal menikahkan.\n
ghāta: m.  pembunuhan, penghancuran, perampokan, algojo, pembunuh.\n
ghātaka: a.  yang bersifat membunuh, mematikan;  m.  pembunuh, algojo, penghancur;  nt.  pembantaian, perampokan, penyamunan, pembegalan.\n
ghāteti: membunuh, membantai, menyembelih, menjagal, memotong.\n
ghāyati: 1. menghidu, membaui, mencium; 2.menjadi terkuras, kehausan.\n
ghora: a.  mengerikan, menakutkan, dahsyat.\n
ca: apa saja; siapa saja; dan, kemudian, maka, lantas (**c’eva** juga, pun); tetapi (**yadā ca** namun bila); jika (**na ca** jika tidak; _ahaṁ ca kho …. pavāremi na ca me bhagavā kiñci garahati_ jika Sang Bhagawan tidak menyalahkan saya.)
cakka: nt.  roda, jentera, cakram, cakra, diskus; bagian, kumpulan, lingkaran, putaran, daur, kalangan, wilayah, kelompok, daerah; kendaraan, sarana, cara, atribut, kualitas; keadaan, kondisi; wibawa, wewenang; **~bheda** m. menghancurkan kewibawaan atau kerukunan atau keharmonisan (keselarasan), menabur perselisihan atau perpecahan; pembangkangan; **~vāḷa** m. nt.  cakrawala, lingkaran (dunia), lengkungan, serangkaian penyangga yang melingkari dunia; pl. sistem dunia. [cakra/cakram Ü Skt. cakra]
cakkavattin: a.  kaisar agung. [cakrawati ← Skt. cakravartin]
cakkhu: nt.  mata; **~bhūta**nt. bermata celik.\n
cakkhumant: a.  yang memiliki mata, yang celik (kelih), yang mampu melihat, berpenglihatan jernih, yang memiliki intuisi atau kebijaksanaan jernih; yang berpengetahuan.\n
caṅkamati: berjalan mondar-mandir, berjalan bolak-balik.\n
caccara: nt.  simpang jalan.\n
cajati: melepaskan, meninggalkan, menyerahkan, mengorbankan.\n
caṇḍa: a.  ganas, galak, garang, bengis, kejam, pemarah, emosional, bernafsu, penuh gairah.\n
catu(r: ) a.  empat.\n
caturassa: a.  persegi, bersegi empat.\n
catuttha: a.  yang keempat; **catutthaṁ**adv.  untuk keempat kalinya.\n
catura: a.  pandai, cerdik, terampil.\n
catta: (pp dari **cajati**)  telah diserahkan, dikorbankan, dilepaskan, direlakan.\n
cattāri: nt.  empat.\n
cattārīsa: (**cattāḷīsa**) empat puluh.\n
canda: m.  candra, bulan, rembulan;  **~vāra**m.  Hari Senin. [candra Ü Skt. candra]
caraṇa: nt. pengembaraan, perilaku, tindakan, kelakuan, tindak-tanduk, langkah, kaki.\n
carati: berjalan-jalan, mengembara, menjelajahi, bergerak, berpindah, bepergian, pergi, pergi mencari makanan; bertindak, berperilaku, melakukan, melakoni, mempraktikkan, menjalankan, mengamalkan.\n
carita: (pp dari **cāreti**)  1. a. yang berlangsung, menyerupai, bertingkah seperti; 2. nt. tindakan, perilaku, kehidupan.\n
cariya: nt.  (**cariyā** f.) tindakan, perbuatan, kehidupan, keadaan, kelakuan, perilaku.\n
calati: menggerakkan, mengaduk, menggetarkan, bingung, ragu-ragu, guncang.\n
cavati: berpindah, beranjak, meninggal.\n
cāga: m. hal meninggalkan˴ menanggalkan˴ melepas˴ merelakan˴ mengikhlaskan; kemurahan hati.\n
cāraka: (**cārika**) a.  berkelana, hidup, pergi, berperilaku; **cārikā** f. perjalanan, pengembaraan, penjelajahan.\n
cāritta: nt.  praktik, pelaksanaan, pengamalan, cara bertindak, tindak-tanduk; _cārittaṁ āpajjati_ bercampur dengan, datang kepada, bersenggama dengan.\n
cārin: a.  berjalan, hidup, mengalami, bertindak, mengamalkan, mempraktikkan, melaksanakan.\n
cāleti: (kaus. dari **calati**) menggerak-gerakkan, menggoyang-goyangkan, mengguncangkan, menghambur-hamburkan, mengayak.\n
cāvanā: f.  pemindahan, penggeseran, penyingkiran, kelenyapan.\n
cāveti: menjatuhkan, menggerakkan, mengusir, mengganggu, mengalihkan, memindahkan, menyingkirkan, menggeser.\n
cikkhala: a.  becek;  nt.  lumpur, luluk, rawa, paya, tanah becek.\n
cikkhalla: nt.  lumpur; rawa, paya; a. becek.\n
cikkhassati: mau menetes, mengalir keluar.\n
ciṅgulaka (ciṅgulika): m. nt.  1. sejenis tanaman; 2. kincir (kitiran) angin mainan.\n
ciṇṇa: (pp dari **carati**) telah dijalani, ditapaki, dilakukan, dilaksanakan, dipraktikkan, menjadi kebiasaan.\n
citta: nt. batin, pikiran, kesadaran, citta (faktor utama batin yang menyadari atau mengetahui suatu objek); niat (_Ahosi te pubbe cittaṁ ‘ārāmaṁ gamissāmī’ti? _Bukankah sebelumnya Anda ada niat pergi ke taman dulu?); [menurut Buddhaghosa citta mempunyai makna (1) Yang mengetahui, menyadari objek (_Cintetīti _**_cittaṁ,_**_ ārammaṇaṁ vijānātīti attho_) \\uf0de  sebagai aktor/agen; (2) Karena/melalui inilah dhamma-dhamma yang menyertainya mengetahui (_Cintenti vā etena karaṇabhūtena sampayuttadhammāti cittaṁ_) \\uf0de  sebagai perantara; (3) Atau sekadar ‘hal mengetahui’ saja (**_Atha vā cintanamattaṁ cittaṁ_**) \\uf0de  sebagai proses;] **~rūpaṁ** sebagaimana yang dipikirkan, sejauh yang diharapkan.\n
citta (citra): a.  aneka ragam, bermacam-macam, bergambar, _bercitra_, elok, enak, manis, berbumbu; nt. lukisan, citra; m. nama bulan. [citra ← Skt. citra]
cinteti (ceteti): menyadari, _mengetahui_; berpikir, merenung, berpendapat; memikirkan, membayangkan, merencanakan, merumuskan, mempunyai niat; (**ceteti**) memikirkan, menghendaki, berniat untuk, berupaya, menginginkan.\n
cira: a.  lama, panjang; **~ṭṭhitika**bertahan lama.\n
cīra: nt.  kulit kayu, serat, busana kulit kayu, rajutan; bilah.\n
cīvara: nt.  jubah, kain.\n
cuṇṇa: a.  yang hancur lebur; nt. bubuk, serbuk, debu, pasir, bedak, pupur.\n
cuta: (pp dari **cavati**)  berpindah, enyah, lenyap, meninggal.\n
cuti: f.  hal berpindah, meninggal; kelenyapan, kepudaran. [cuti ← Skt. cyuti]
cuddasa: a.  empat belas.\n
cumbaṭa: nt.  lilitan kain bantalan beban di kepala; gelung bantalan; karangan bunga, rangkaian bunga (berbentuk lingkaran).\n
ce: jika, tetapi.\n
cecca: = **sañcicca**
cetaṁ: 1. **ca etaṁ**dan ini; 2. **ce taṁ**jika itu.\n
cetanā: f.  niat, pikiran, tujuan, _kehendak_, hasrat.\n
cetayati:  = **cinteti**
cetasā: bentuk instr. dari ceto.\n
cetasika: a.  mental, batiniah (_cetasika-dukkha,  cetasika-sukha_);  nt. yang tercakup dalam batin (_ceto_), yang dimiliki batin, faktor mental, corak batin, pengiring batin (_citta_).\n
cetaso: bentuk gen. dari ceto.\n
cetiya: nt.  tempat pemujaan; monumen berkubah sebagai tempat pemujaan (keramat); pagoda.\n
ceto: nt.  = **citta**
cetopaṇidhi: f.  = **paṇidhi**.\n
codeti: mendesak, mendorong, menghasut; memarahi, mengomeli, mencaci, mengumpat, mempertanyakan, menagih.\n
cora: m.  pencuri, maling, alap-alap, perampok, penyamun, garong, pencoleng, penjarah; **~ghāta** m. algojo pencuri. [curi ← Skt. √cur]
corī: f. pencuri atau maling wanita.\n
cola (coḷa): m.  sepotong kain, perca, carik kain.\n
chakala: m.  kambing jantan; **chakalī** (f.)
chaṭṭha: keenam, ke-6, VI.\n
chaḍḍeti: meludahkan, memuntahkan, mencampakkan.\n
chaṇa: m.  festival, perayaan, _pesta_, _kenduri_.\n
chatta: 1. nt. sejenis payung tetapi gagangannya ada di tepi bukan di tengah; kanopi; 2. m. siswa (pemegang payung gurunya).\n
chanda: m.  hasrat, dororngan hati, niat, dambaan, kehendak, keinginan (untuk berbuat), impuls, antusiasme, minat, kegairahan, nafsu, kesukaan; persetujuan, perkenan; ikhlas, suka hati.\n
channa: a.  tertutup, diberi atap, disembunyikan, tersembunyi, rahasia; cocok, patut, pantas, sesuai.\n
chamā: f.  tanah, bumi; adv. di atas tanah, ke tanah.\n
chambhitatta:  (nt.) keadaan kaku, lumpuh, takut, gentar tak berdaya.\n
chavi: f.  kulit (tipis), pemalut.\n
chādeti: 1. menutupi, menyembunyikan; (suara) memenuhi, merasuk; 2. tampak bagus, menyenangkan; senang dengan, suka akan.\n
chāpaka: m. anak kecil dari hewan, hewan belia.\n
chāyā: f.  bayangan; **~rūpa** nt. potret, foto. [cahaya ← Skt. chāyā]
chārikā: f.  abu.\n
chidda: a.  bercelah, berlubang-lubang; bercacat; nt.  celah, lubang; cacat.\n
chindati: memotong, mengudung (memotong ujungnya; mengerat tangan, jari dsb); menorehkan, memancung, memenggal, menghancurkan, menyingkirkan.\n
chinna: (pp dari **chindati**)  terpotong, terpancung, terpenggal, dihancurkan; ceruk.\n
chinnikā: f.  penipu, pendusta, pembohong, yang palsu, yang memperdayakan, yang curang, lihai, licik, culas; liar.\n
chupati: menyentuh, menyinggung, menyenggol.\n
chupana: nt.  sentuhan, singgungan, senggolan.\n
chupita: (pp dari **chupati**) disentuh.\n
cheka: a.  pandai, terampil, mahir; asli.\n
chejjabhejja: a. penyiksaan dan pemuntungan.\n
cheppā: f.  ekor.\n
jaṅgala: nt.  tempat yang kasar, berpasir dan tidak berair, tanah tandus; hutan, rimba, jenggala. [jenggala ← Skt. jaṅgala]
jaṅghā: f.  tungkai bawah (antara lutut dan tumit); **jaṅghapesanika**m.  pesuruh (pengantar pesan) (yang berjalan kaki).\n
jacca: a.  kelahiran, darah keturunan, keturunan, strata sosial.\n
jaṭā: f. kekusutan, jalinan, anyaman, kepang, kelabangan; rambut beranyam, kusutan ranting pohon; kusutan nafsu.\n
jana: m.  makhluk hidup, orang, individu; **mahā~** orang banyak; **bahu~** banyak orang, kebanyakan orang; **nānā~** pelbagai makhluk hidup; **keci janā** sejumlah orang.\n
janatā: f.  kumpulan orang, orang-orang, jemaah, orang banyak; publik, rakyat.\n
janati: kaus. **janeti** (**janayati**) atau **jāneti**menghasilkan, melahirkan, menyebabkan, menerbitkan, menimbulkan.\n
jananī: f.  ibu.\n
janapada: m.  negeri hunian, negara, benua, propinsi, daerah (pemerintahan), distrik, wilayah, udik; **~cārikā** penjelajahan negara.\n
janita: (pp dari **janati**)  dilahirkan, dihasilkan.\n
janettī: f.  ibu kandung.\n
jantāghara: m.  ruang atau kamar sauna, ruang tamu atau duduk.\n
jambu: f.  jambu (_Eugenia jambolana_); jambu mawar (KBBI: _Syzygium jambos_). [jambu ← Skt. jambu]
jayati: menaklukkan, mengalahkan, mengungguli; menjarah, merampas; pass. **jīyati**.\n
jarati: meluluh, menjadi tua.\n
jarā: f.  pelapukan, usia tua.\n
jalati: membakar, menyala, bercahaya; kaus. **jaleti** (**jāleti**) menyalakan.\n
jahati (jahāti): meninggalkan, melepaskan, menanggalkan.\n
jāgara: a.  terjaga, sadar, awas, waspada.\n
jāgarati: terjaga, sadar, awas.\n
jāta:  (pp dari **janati/janeti**)  lahir, tumbuh, muncul, dihasilkan; yang dilahirkan; “asli”, alamiah, benar, bagus; menjadi, terjadi; setelah menjadi, seperti, sejenis; n. kumpulan, himpunan; **~rūpa**m. logam murni, emas (yang belum diolah; yang sudah diolah ▶ **suvaṇṇa**).\n
jātaka: nt.  cerita atau kisah kelahiran, kisah kehidupan lampau (Sang Buddha); judul buku (kitab) ke-13 dari _Khuddaka-nikāya_ yang berisikan 547 kisah kelahiran lampau Sang Buddha; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**);  m.  putra, anak.; nt.  kisah kelahiran lampau Sang Buddha; judul buku ke-13 dari _Khuddaka-nikāya_; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**)
jāti: f.  kelahiran, kelahiran kembali; suku bangsa; negara, silsilah keturunan, darah keturunan; status sosial, kasta; jenis, macam.\n
jātika: a.  seperti, dari, memiliki, bersifat, bertabiat, berwatak, yang; keturunan dari, berstatus sosial, tergolong kelas.\n
jāna: a.  mengetahui, dapat diketahui, dapat dipahami; secara sengaja.\n
jānāti: memahami, mengetahui, mencarikan, menemukan, menyadari; pass. **jānīyati**, **ñāyati**.\n
jānu: nt.  lutut, dengkul; **~maṇḍala**tempurung lutut.\n
jāyati (jāyate) :  dilahirkan, dihasilkan, muncul, dilahirkan kembali.\n
jāyā: f.  istri.\n
jāra: m.  kekasih gelap, gundik, selir, pezina.\n
jāla: 1. nt. jala, jaring-jaring, siratan, rajutan, jerat, perangkap, tipuan, maya (khayalan); 2. m. nyala (api), sinar, cahaya.\n
jālā: f.  nyala api.\n
jālin: a. berjala, terjalin, menjerat, memperdayakan; nelayan.\n
jigiṁsati: (desid. dari **jayati**)  menginginkan, menghendaki, mendambakan, ingin mendapatkan, berhasrat akan.\n
jiṇṇa: (pp dari**jarati**)  berusia renta, tua-renta; tua rapuh; dicerna. (_jajjarībhūte jarāya khaddiccādi-bhāvaṁ āpādite; cirakālappavattakulanvaye_)
jina: m.  pemenang, yang telah menaklukkan, Buddha.\n
jināti: ☞  **jayati**
jīva: a.  jiwa, nyawa, roh; makhluk berjiwa; nt. burung _jīvaka_. [jiwa ← Skt. jīva]
jīvati: hidup, hidup dengan.\n
jīvikā: f. hidup, penghidupan.\n
jīvita: nt.  hidup, masa hidup, kehidupan, kelangsungan hidup, mata pencaharian, penghidupan, nyawa; _jīvitaṁ kappeti_ menjalani hidup; **~indriya**nt. daya hidup, daya pengendali kelangsungan hidup.\n
jivhā: f. lidah; pengecapan.\n
jūta: nt.  permainan, permainan dam, permainan dadu, perjudian.\n
je: (kata seru)  oh, ah, he, wah; panggilan terhadap budak wanita di Wesali kuno.\n
jigucchati: menghindari, merasa muak terhadap, takut terhadap, ogah terhadap, sebal terhadap.\n
jeguccha (jegucchiya): a.  memuakkan, menyebalkan, menjijikkan.\n
jegucchin: m.  orang yang merasa muak, ogahan, sebal.\n
jeṭṭha: a.  yang tertua, sulung, yang tersenior, yang tertinggi, yang lebih baik, yang terbaik, yang pertama, yang jempolan.\n
jeti: ☞  **jayati**
jotaka: .  a.  menjelaskan, menerangkan, mengungkapkan.\n
joti: m. nt.  cahaya, semarak, sinar, seri; bintang; api; **sajotibhūta**menyala, terbakar.\n
jhāna: nt.  meditasi; keadaan batin yang terserap (absorpsi); tingkatan atau taraf pencapaian meditasi; jhana.\n
jhāpeti: (kaus. dari **jhāyati**)  menyulut, membakar, memasak; menghancurkan, meruntuhkan, membunuh.\n
jhāyati: 1. bermeditasi, berkontemplasi, merenungkan; memburu, mengincar, mencermati; 2. terbakar, aus, mengering; menyulut.\n
jhāyin: a.  merenung, bermenung, tepekur, bermeditasi.\n
ñatti: f.  pengumuman, pemakluman, pernyataan, mosi, usul, resolusi; **~catuttha**  satu mosi + tiga resolusi.\n
ñāṇa: nt.  _pemahaman_, pengertian, pengetahuan, kebijaksanaan, pengetahuan hasil penilikan batin.\n
ñātaka: m.  sanak keluarga, famili, kerabat.\n
ñāti: m.  sanak famili, kerabat, keluarga; **~vyasana** nt.  musibah kehilangan sanak keluarga.\n
ñāpeti: (kaus. dari **jānāti**)  mempermaklumkan, menjelaskan, mengumumkan.\n
ñāya: m.  cara, metode, kebenaran, sistem, logika; cara atau perilaku yang benar/ sesuai.\n
ṭhapita: (pp dari **ṭhapeti** atau **ṭhapāpeti**) telah diletakkan, ditegakkan, dibangun, didirikan, ditaruh, ditempatkan.\n
ṭhapeti: (kaus. dari **tiṭṭhati**)  meletakkan, mendirikan, memasang, menyusun, membangun, menegakkan, menempatkan, menentukan, menyimpan, mengabaikan, mengesampingkan; **ṭhapetvā** di samping itu, kecuali.\n
ṭhāna: nt.  tempat (yang memungkinkan), daerah, wilayah; kondisi, keadaan; sifat, kualitas, tingkatan; lokasi; objek, hal, pokok, dasar, cara, alasan, dalih, penyebab; _ṭhānaṁ etaṁ vijjati_  bisa saja terjadi, mungkin saja. [tanah ← Skt. sthāna]
ṭhānaso: adv.  tanpa bergerak, tanpa jeda atau penyebab (perubahan); segera; langsung; sekarang juga, secara spontan, saat itu juga, seketika itu juga.\n
ṭhāniya: a.  berdiri, memiliki tempat berpijak, disebabkan oleh, (kondisi) yang menimbulkan, mempunyai dasar pijakan.\n
ṭhita: a.  berdiri, tegak tidak bergerak, kokoh, mantap, yang berdiam dalam.\n
ṭhiti: f.  keadaan kestabilan, kemantapan, kelangsungan, kelanggengan, kelestarian, hal bertahan; posisi, kedudukan; persinggahan, pangkalan, stasiun.\n
ḍasati: menggigit (oleh lalat, ular, kalajengking, dsb), menyengat.\n
ta: ia, itu, ini, di sana; oleh sebab itu, karenanya, lantas.\n
takka: 1. m. kesangsian, pandangan yang penuh kesangsian (=**diṭṭhi**), pertimbangan yang terlampau teliti, cara berpikir yang tidak masuk akal, pemikiran; 2. nt. susu mentega (cairan susu yang tinggal setelah membuat mentega) dengan ¼ bagian air (dibuat dengan mengaduk-aduk dadih), termasuk salah satu dari lima produk sapi (_pañca-gorasā_ : _khīra_, _dadhi_, _takka_, _navanīta_, _sappi_).\n
taṁkhaṇika: a.  sementara, sesaat, pada saat itu.\n
taca: (taco nt.)  m.  kulit (tebal), jangat.\n
taccha: 1. m. tukang kayu; 2. a. benar, betul, nyata, sungguh; nt. kebenaran.\n
tacchaka: m.  1. tukang kayu; pembangun; 2. sejenis Naga; f.  **tacchikā** wanita berstatus sosial rendah (= **veṇī**, perajin bambu).\n
tajja: a.  dari sana, bersuaian, sehubungan dengan ini/itu, berdasarkan ini/itu.\n
taṇḍula: m.  beras.\n
taṇhā: f.  haus, dahaga; idam, damba, kehausan akan, nafsu dambaan. [tresna ← Skt. tṛṣṇā]
tatiya: a. ketiga; **tatiyaṁ** untuk ketiga kalinya.\n
tato: dari situ, dari sana, lantas, kemudian, selanjutnya.\n
tatta: 1. (pp dari **tapati**) panas, dipanasi, memijar, membara; 2. nt. kebenaran.\n
tattha: adv.  di sana, di tempat itu; dalam hal itu, sehubungan dengan itu, untuk itu; **tattha** **tattha**di sana sini.\n
tatra: di sana; dalam ini; di sana-sini, dalam ini dan itu, dalam kondisi apa pun, segala macam, segenap, total (**tatramajjhattatā**keseimbangan total); **tatra tatra** di sana-sini, dalam ini dan itu; **tatra sudaṁ**di sana).\n
tatha: a.  benar, betul, nyata.\n
tathā: adv. demikian, seperti ini, begitu, begini; _tathūpamaṁ_  seperti itu; **tath’eva**demikian pula, hanya begitu, masih tetap sama, tidak berbeda, di tempat itu juga; maka; **tathā yathā** sedemikian rupa …..sehingga.\n
tathāgata: salah satu sebutan untuk Sang Buddha.\n
tadā: adv.  ketika itu, saat itu, pada waktu itu (= **tasmiṁ samaye**); **tadāhaṁ**waktu itu saya.\n
taduttari: lebih dari itu.\n
tanu: a.  kurus, ceking, kecil, langsing, ramping, lampai, lembut; badan, tubuh.\n
tandī: f. kelesuan, kemalasan, kelambanan.\n
tapa (tapo): m. nt.  siksaan, hukuman, penebusan dosa, pengekangan diri, penghukuman diri, tapa-brata; kebaktian, ketakwaan, pengendalian diri, praktik moralitas. [tapa ← Skt. tapa]
tapati: bercahaya.\n
tapanīya: a.  membakar, menghanguskan, menyiksa, melakukan penyiksaan diri, mengekang diri, menimbulkan kemuakan, menekan hawa nafsu; mengkilap bercahaya;  nt. emas.\n
tapassin: m.  orang yang bertapa-brata, pertapa, orang yang berlatih pengendalian diri dan mampu mengendalikan indria
tappati: 1. (pass dari **tapati**) membakar, tersiksa; 2. dipuaskan, terpuaskan, dibuat senang, terpenuhi; kaus. **tappeti** memuaskan, menghibur, menyuguhi, memberi makan, menikmati.\n
tama: m. nt.  kegelapan.\n
taraccha: m.  hiena (_Hyaenidae_), dubuk (_Hyaena crocutus/striata_).\n
tarati: melewati, melintasi, mengarungi, mengatasi, melampaui, menanggulangi; buru-buru, tergesa-gesa, cepat-cepat, tergopoh-gopoh.\n
taruṇa: a.  empuk, muda, remaja, halus, baru, segar; tunas, taruk, kecambah. [teruna ← Skt. taruṇa]
taruṇī: f.  gadis, remaja wanita.\n
tala: nt.  permukaan datar, permukaan, tanah, dasar, lapisan; telapak tangan atau kaki. [tala ← Skt. tala]
taluna: = **taruṇa**
taḷāka: nt.  kolam, telaga, waduk, balong. [telaga ← Skt. taṭaka/taṭāka/taḍāga]
tasati: 1. haus, mendambakan; 2. gemetar, gentar, takut, menjadi ketakutan.\n
tasmā: oleh karena itu.\n
tahiṁ: di sana.\n
tāṇa: nt.  perlindungan, pernaungan, terlindung dari.\n
tāta: ayah, papa, bapak; sebutan kasih atau ramah atau penuh hormat untuk orang yang lebih muda atau tua, lebih rendah atau tinggi statusnya.\n
tādisa: a.  seperti itu, semacam itu; seperti Anda.\n
tādisaka: a. bersifat seperti itu.\n
tāpasa: m. petapa.\n
tāpeti: (kaus. dari **tapati**)  membakari, memanasi, menghangatkan, menghanguskan, menyiksa, (meleburkan).\n
tāreti: (kaus. dari **tarati**)  menyeberangkan, membantu, membantu melewati, menolong.\n
tāla: m.  pohon lontar, siwalan, tal (_fan palm_, _Borassus flabeldiformis_); **~pakka**nt. buah siwalan. [tal ← Skt. tāla]
tāḷa: 1. m. pemukulan, penghantaman, benda yang dipukul, alat musik tabuhan misalnya gong (canang besar), canang, gembreng (canang yang tidak bertombol di tengah-tengah), atau rebana; musik; 2. nt. kunci; **~chidda**nt. lubang kunci. [tala ← Skt. tāla]
tāḷeti: memukul, menghantam, menggebuk, mencambuk.\n
tāva: adv.  sebegitu, sejauh, sepanjang; pertama-tama; dikarenakan, sebab; sebagaimana, seperti, begitu; biarkan; masih; **~kālika** a. (untuk) sementara (waktu).\n
tāvadeva: baru saja, segera, di situ juga, saat itu juga, ketika itu; = **tadā eva** = **tāvade**.\n
ti: a.  tiga.\n
tiṁsati: (**tiṁsā**) f.  tiga puluh.\n
tikkha: a.  tajam, pandai, cerdik, cermat, tangkas, cerdas.\n
tiṭṭhati: berdiri, berhenti, stop, berdiam, tinggal, berkukuh, tetap, senantiasa (terus-menerus), bertahan (_Buddhasāsanaṁ ciraṁ tiṭṭhatu  _semoga ajaran Buddha bertahan lama), berlangsung, meletakkan, meninggalkan, membiarkan (_tiṭṭhatu pubbanto tiṭṭhatu aparanto_ tinggalkan yang sudah lewat, biarkan yang akan datang; _tiṭṭhatu bhikkhave satta-vassāni, yo hi koci bhikkhave ime cattāro satipaṭṭhāne evaṁ bhāveyya cha vassāni  _tak usah tujuh tahun).\n
tiṇa: nt.  rumput, herba (tumbuhan terna), terna (tumbuhan dengan batang lunak tidak berkayu atau hanya mengandung jaringan kayu sedikit sekali sehingga pada akhir masa tumbuhnya mati sampai ke pangkalnya tanpa ada bagian batang yang tertinggal di atas tanah), rumput-rumputan, lalang, jerami, rumput kering, sampah. [terna ← Skt. tṛṇa]
tiṇṇa: (pp dari **tarati**)  yang telah mencapai pantai seberang; telah melewati, telah mengatasi, telah menyeberangi, telah mencapai Nibbana.\n
tiṇha: a.  tajam.\n
titikkhā: f.  kesabaran atau ketabahan atas penderitaan, hal kelapaangan hati untuk memaafkan.\n
tittaka: a.  tajam, (rasa) pahit, getir (pahit + pedas).\n
tittira: m.  semacam ayam hutan, (_partridge_; _Perdix cinerea; Caccabis rufa_), ketitir?, perkutut? (_Geopelia striata_)
tittha: nt.  arungan, tempat menyeberang, tempat mendarat, tempat mck; sekte (ajaran sesat). [tirta ← Skt. tīrtha]
titthiya: m.  pengikut aliran lain, pengikut ajaran sesat.\n
tinta: a.  basah, lembap.\n
tibba: a.  tajam, menggebu-gebu, antusias; padat, tebal, rimbun, bingung, gelap, remang-remang.\n
timbaru (timbarūsaka): sejenis mentimun (_Strychnos_ _nux vomica_ atau _Diospyros_), _kesemek_ (_Diospyros_ _kaki_). [Kayu ular (_Strychnos ligustrina_)]
tiracchāna: m.  hewan, binatang; rendah, murahan; **~gata**hewan; binatang (buas).\n
tiriyaṁ: adv.  secara melintang, horizontal, mendatar, melebar, menyamping.\n
tiro: a.  seberang, di luar, di atas, di sana, jauh; **~karaṇī** f. tirai, selubung, tabir; **~gāma** m. perkampungan luar, dusun lain atau seberang, perkampungan jauh.\n
tirokkha: a.  yang berada di luar, absen, tidak hadir; **~vāca** omongan menghina atau menyepelekan.\n
tila: m. nt.  tanaman atau biji wijen.\n
tilaka: m. 1. noktah, titik, tahi lalat, bintik; 2. sejenis pohon.\n
tīṇi: nt.  tiga.\n
tīreti: (kaus. dari **tarati**) mengatasi, menyelesaikan, membereskan, melaksanakan; mengukur, menilai, (mengakui, mengenal, menghargai).\n
tu: namun, tetapi, sekarang, maka; **kin** **tu**tetapi; **tv** **eva**namun.\n
tuccha: a.  kosong, hampa, sepi. (=**tucchaka**)
tuṇhī: diam (seribu basa), bergeming, membisu, berdiam diri (_tuṇhimāsīne_  kala duduk diam);  **~bhāva**m.  diam membisu, diam tidak bersuara.\n
turati: (= **tarati**) bergesa-gesa, cepat-cepat, buru-buru.\n
turita: (pp dari **turati**) tergesa-gesa, kesusu, cepat-cepat.\n
tulā: f.  gandar untuk mengangkat, membawa atau menopang; kasau; gandar timbangan, timbangan, neraca; ukuran, patokan, standar, berat, bobot; tingkatan, bandingan; ukuran berat (= 100 **pala**).\n
tuvaṭaṁ: adv.  dengan cepat.\n
tuvaṭṭeti: berbagi.\n
tuvaṁ: (**tvaṁ**) engkau, Anda. [tuan ← Skt. tvam]
teja (tejo): m.  “ketajaman”, panas, nyala, api, cahaya, sinar, seri, kecemerlangan, semarak, energi, kekuatan, daya.\n
temeti: membasahi.\n
tela: nt. minyak wijen, minyak.\n
thaketi: menutup (pintu, jendela, dan sebagainya).\n
thañña: nt.  air susu ibu.\n
thambha: m.  pilar, tonggak, tiang, saka; keras kepala, kemunafikan, egois, bandel, angkuh, keras, kokoh; rumpun rumput.\n
thambheti (upatthambheti): membuat tegar, membuat tegang, meregang, menopang, menyokong, menggalang, menyangga; _kāyaṁ thambheti_  meregang diri.\n
tharaṇa: nt.  tebaran, bentangan, paparan, arungan; lapik, pengalas.\n
tharu: m.  pangkal (gagang) senjata atau pedang; pedang.\n
thala: m.  dataran (kering) (yang tinggi atau keras); lapangan, padang.\n
thavikā: f.  ransel, buntil(an), pundi-pundi, kantong (terutama untuk membawa saringan air dan patta).\n
thāma: m.  kekuatan, daya, kemampuan.\n
thālaka: nt.  cangkir, gelas.\n
thālī: .  f.  belanga, ceret, kuali yang terbuat dari tanah; **~pāka**m. persembahan barli atau nasi yang dimasak dalam susu, santapan barli susu.\n
thāvara: a.  berdiri diam, tidak bergerak, kokoh, kuat, stabil, tertambat; yang sudah tidak memiliki haus-damba atau nafsu keinginan, yang sudah mencapai kesucian.\n
thāvariya: nt.  kekokohan, kemantapan, keamanan, ketaktergoyahan, ketenteraman.\n
thira: a.  kokoh, kukuh, kuat, mantap, perkasa, tangguh, tegar, tahan lama, keras, awet.\n
thiratā: f.  kemantapan, ketegaran, stabilitas, keteguhan, ketangguhan; tiada geming.\n
thīna: nt. hal kaku, tidak tanggap, tak peduli, tak sigap; **~middha** lesu-lamban.\n
thūla (thulla): a. pampat, masif, kasar, besar, kuat, berat; umum, biasa, rendah;  **~accaya**m. pelanggaran serius, pelanggaran berat.\n
thena: m.  pencuri;  a.  mencuri.\n
theyya: nt.  pencurian; **~citta** pikiran untuk mencuri; **~saṅkhātaṁ**adv.  dengan cara mencuri, dengan cara yang dianggap sebagai mencuri.\n
thera: a.  senior, terkemuka.\n
thoka: a.  kecil, sedikit, pendek, remeh;  nt. secuil, sekelumit.\n
thometi: memuji, menyanjung, mengagungkan.\n
daka: nt.  = **udaka**
dakkha: a.  cakap, terampil, cekatan, mampu, pandai, piawai; nt. kecekatan, kemampuan, keterampilan. [daksa ← Skt. dakṣa]
dakkhiṇa: a.  kanan; terampil, cekatan, tangkas; selatan. [daksina ← Skt. dakṣiṇa]
dakkhiṇā: f.  ‘yang diberikan dengan tangan kanan’, hadiah, derma, persembahan, buah tangan (yang diberikan kepada seorang ‘suci’ untuk menolong arwah leluhur); honor.\n
dakkhiṇeyya: a.  yang layak menerima persembahan atau buah tangan.\n
daṭṭha: (pp dari **ḍasati**)  digigit, disengat.\n
daḍḍha:  ( pp dari **dahati**)  terbakar.\n
daṇḍa: m.  tangkai pohon, kayu, gagangan; tongkat, batangan, penopang; hukuman, deraan (dengan tongkat); tongkat pemukul, tembung (tongkat pemukul atau penangkis [sebagai senjata berkelahi]), pentungan; denda. [denda ← Skt. daṇḍa]
daṇḍaka: m.  tongkat (kecil), tangkai, batang, gagang;  **aḍḍha~**m.  tongkat pendek untuk memukul, pentung.\n
daṇḍī: nt.  pengembara.\n
dadāti: memberi, menghadiahkan, mengagih, mendermakan, mempersembahkan, bermurah hati kepada; membolehkan; _okāsaṁ ~_ memberi kesempatan, membolehkan; _jīvitaṁ ~_ mengorbankan jiwa; pass. **diyyati, dīyati**.\n
dadhi: nt.  dadih, susu beku, susu kental. [dadih ← Skt. dadhi]
danta: 1. a.  terbuat dari gading;  m.  gigi, gading, taring;  **~poṇa**nt. tusuk gigi; 2. (pp dari **dameti**)  dijinakkan, dikendalikan, ditaklukkan.\n
damana: a.  menjinakkan, menaklukkan, menguasai.\n
dameti: menjinakkan, menghukum, mengendalikan, menguasai, menaklukkan, menundukkan, mengubah, mengkonversi.\n
dalidda (daḷidda): a.  orang gelandangan, pengembara, miskin, papa, melarat, fakir, pengemis, peminta-minta. [derita? ← Skt. daridra]
daḷha: a.  kuat, kokoh, perkasa, kukuh, tangguh, kekar, mantap; nt. adv. sangat, amat, dengan kuat, kencang.\n
dava: m.  1. api, panas; 2. berlari, meluncur, berpacu, jalan, terbang, kecepatan, bermain-main, bergurau, iseng.\n
dasa: a.  sepuluh. [dasa ← Skt. daṡa]
dassa: m.  melihat atau tampak, mencerap atau tercerap.\n
dassati: (**dakkhati, dakkhiti**) melihat.; fut. dari **dadāti**.\n
dassana: nt.  hal melihat, memandang; persepsi, pandangan, penglihatan, penilikan (batiniah).\n
dassanīya: a.  elok dipandang, cantik, indah, sedap dipandang mata, seronok.\n
dasseti: (kaus. dari **dassati**) mempertunjukkan, memperlihatkan; **dassetuṁ** inf. menunjukkan, memperlihatkan, menjelaskan, mengisyaratkan, mempertontonkan.\n
daha: m.  danau.\n
dahati: 1. (= **dahate**) menempatkan, berkukuh pada, meletakkan, mengira, menganggap, mencamkan, menyatakan; 2. (= **ḍahati**) membakar.\n
dahara: a.  kecil, mungil, lembut, muda; anak muda, pemuda, anak laki-laki, remaja.\n
dāṭhā: f.  gading, gigi taring, gigi yang besar.\n
dāṭhin: a.  yang mempunyai gading; gajah.\n
dāna: nt.  pemberian, hadiah, derma, kemurahan hati, dana.\n
dānava: m. sejenis asura atau raksasa, keturunan Danu.\n
dāni: adv.  sekarang, kini.\n
dāpeti: 1. membuat seseorang memberi, menyuruh memberi; membagi, mengirim, memberi, mempersembahkan; 2. melarikan, membuat lari.\n
dāya: m.  1. kayu, hutan, rimba, belukar, hutan kecil, taman; 2. hal memberi, hadiah, dana, derma, sumbangan, imbalan, bagian, bayaran.\n
dāyaka: a.  memberi, menganugerahi, membagi; m. penderma, dermawan.\n
dāyajja: nt.  warisan, ahli waris.\n
dāra (dārā): f.  wanita muda, dara, istri, wanita yang telah menikah. [dara Ü Skt. dārā]
dāraka: m.  bocah, anak-anak, pemuda, kanak-kanak.\n
dārikā: f.  gadis, putri.\n
dāru: nt.  kayu; potongan kayu; pl. bagian-bagian (yang terbuat dari) kayu; **~gaha**m.  gudang kayu; **~dhītalikā**f.  boneka kayu.\n
dāsa: m.  budak, hamba, jongos, bentara, abdi.\n
dāsī: f.  budak atau hamba wanita.\n
diṭṭha: (pp dari **dassati**) terlihat, tampak;  nt.  penglihatan;  **~dhamma** dunia ini, kelahiran ini, keadaan ini, keberadaan ini.\n
diṭṭhi: f.  pandangan, paham, kepercayaan, spekulasi (pandangan salah).\n
diṭṭhika: a.  hal melihat atau memandang, seseorang yang beranggapan; (seseorang) yang berpandangan atau berpaham.\n
dinna: (pp dari **dadāti**) diberikan, dihadiahi.\n
dibba: a.  dewa, surgawi, supranatural.\n
dibbati: bermain-main, bersenang-senang, beriang-ria.\n
divasa: m. nt.  hari.\n
divā: adv.  siang hari; **~taraṁ**adv. agak siang; **~vihāra**m.  istirahat siang, tidur siang.\n
disā: f.  penjuru, wilayah, daerah, arah, jurusan; (_puratthimā_, _pacchimā_, _dakkhiṇā_, _uttarā_, _uparimā_, _heṭṭhimā_ + 4 _anudisā_)**; diso disaṁ** di semua penjuru.\n
dissati: pass. dari **dassati**.\n
dīgha: a.  panjang, tinggi, panjang lebar;  m. ular; **~jāti**f. ular.\n
dīpa:   1. m. lampu, pelita; 2.  m. nt.  pulau, benua, kontinen, terra firma, landasan kokoh, landasan dudukan, tempat yang aman.\n
dīpin: m.  panter, harimau akar, macan tutul (_Panthera pardus_).\n
dīpeti:  menyalakan, mengobarkan, menyulut, memancarkan cahaya, bersinar; menerangkan, menjelaskan.\n
dukkaṭa: m.  tindakan salah, tindakan tak baik, kesalahan, keburukan.\n
dukkha: nt. duka, penderitaan, kesakitan, ketidaknyamanan, ketidakpuasan, kesusahan, kesengsaraan; hal sakit, menyakitkan. [duka **←** Skt. duhkha]
dukkhita: a.  menderita, tak bahagia, duka, merana, kecewa, penyedihkan, patah hati.\n
dukkhin: a.  menderita, bersedih hati, sengsara, menyedihkan.\n
duggata: a.  dalam kondisi atau alam yang menyedihkan; menyedihkan, tidak bahagia, malang.\n
duggati: f.  alam menyedihkan. ( = **apāya**)
duccara: a.  sukar, sulit.\n
duccarita: nt.  tindakan salah, perbuatan atau perilaku buruk.\n
duṭṭha: (pp dari **dussati**)  dicemari, digerogoti, rusak, buruk, jahat, bejat, busuk, ganas, jorok. [dusta ← Skt.duṣṭha]
duṭṭhulla: a.  jahat, cabul, kotor, berat, serius.\n
dutiya: a.  yang kedua, yang berikut, (sebagai) rekan(an); **dutiyaṁ**adv. untuk kedua kalinya.\n
dutiyikā: f. istri atau perempuan.\n
dupposatā: f.  hal sulit untuk didukung, sulit untuk dipelihara, sulit untuk dirawat.\n
dubbaca: a.  sulit dinasihati, sukar diajak bicara, mendegil, membandel.\n
dubbaṇṇa: a.  berwarna jelek, jelek.\n
dubbalya (dubballa: ) m.  ketidakkuasaan, ketidaksanggupan; **dubbalyā**adv.  tanpa dasar, tanpa bukti kuat.\n
dubbha: a. mencurangi, menyakiti, berusaha melukai; **adubbha**nt. hal tidak menyakiti, keterusterangan, keramahan, niat baik.\n
dubbhaka: a. berkhianat, berdurhaka.\n
dubbharatā: f.  hal sulit untuk disokong, sulit untuk dipelihara.\n
dubbhikkha: a.  dilanda bencana kelaparan;  nt.  kelangkaan makanan sedekah, bencana kelaparan, kekurangan makanan.\n
dummano: nt.  batin yang tertekan, sedih.\n
dummaṅku: a.  terhuyung-huyung, berpikiran jahat.\n
dussa: nt. bahan tenunan, kain, kain serban; busana (atas), pakaian; **~yuga** selengkap pakaian, satu setel pakaian, selengkap sandang.\n
dussati:  menjadi buruk atau jahat, menjadi bejat, menjadi rusak; menjahati, menggerogoti, merongrong, mencemari.\n
dussīla: a.  berakhlak bejat.\n
dūta: m.  utusan, duta, kurir, wakil; pesuruh;  nt. permainan, judi. [duta ← Skt. dūta]
dūteyya: nt.  suruhan, pesan(an), tugas.\n
dūra: a. jauh. [dura ← Skt. dūra]
dūsaka: a.  menggerogoti, membuat aib, menodai; m.  pencemar, penoda, perusak, pembuat aib.\n
dūseti: merusak, menghancurkan; melukai, mencederai; mengotori, mencemari, menodai.\n
deti: ☞ **dadāti**.\n
deyya: a.  diberikan, layak dihadiahi, layak diberi derma; nt. hadiah, persembahan; **~dhamma**m. hadiah, pemberian.\n
deva: m.  “cemerlang, bercahaya”, dewa, dewata; (awan) hujan; raja, paduka; **~gaha**m.  kuil, candi; milik kerajaan. [dewa ← Skt. deva]
devatā: f.  “kondisi atau keadaan suatu dewa”, kedewaan; dewa, dewata, peri.\n
devasika: a.  harian; **devasikaṁ** adv. harian, setiap hari.\n
devī: f.  dewi (dewa wanita), peta wanita, yakkha wanita; ratu, puan, nyonya. [dewi ← Skt. devī]
desa: m.  titik, pokok, bagian, tempat, lokasi, daerah, wilayah, negeri; cakupan. [desa ← Skt. deśa]
desanā: f.  wejangan, instruksi, pengarahan, tuntunan, pelajaran, uraian, pembabaran, ceramah, khotbah; pemakluman, pernyataan; pengakuan, pengesahan.\n
desita: (pp dari **deseti**) dipaparkan, ditunjukkan, diperlihatkan, diajarkan, diberikan.\n
deseti: menunjukkan, memaparkan, mengajar, membabarkan, memperlihatkan, mengungkapkan.\n
doṇa: m.  ember kayu, tong; ukuran takaran (= 4 **āḷhaka**).\n
doṇī: f.  ember kayu, tong; sampan berbentuk ember (beralas datar); lubang atau lembah yang digali di tanah; badan kecapi.\n
domanassa: nt.  ketidakbahagiaan, kekesalan, ketidaknyamanan batin, kesedihan, kepedihan, gundah-gulana.\n
dovacassa: nt.  kerusuhan, kekacauan, kekusutan; bandel, degil, kepala batu, keras kepala, tak mau menurut atau mendengar kata orang, rongseng, cengeng, buruk laku.\n
dosa: m.  gerogotan/rongrongan, cacat, noda, kesalahan, galat, kekeliruan, keburukan, kebejatan, kebobrokan, keadaan tergerogoti atau rusak; kemarahan, kebencian, kedengkian, niat jahat.\n
dohaḷa: m.  mengidam, hasrat yang kuat.\n
dvaya: a.  dua, ganda; salah, keliru, palsu, dusta;  nt.  sepasang, dua sejoli.\n
dvādasa: a.  dua belas.\n
dvāra: nt.  pintu, pintu masuk, gerbang.\n
dvi: a.  dua, ganda, sepasang.\n
dvīhitika: a. sulit mendapatkan, payah memperoleh; gagal panen.\n
dhaja: m.  bendera, panji; lambang, simbol, emblem, lencana; **~gga**puncak panji, puncak rujukan. [duaja ← Skt. dhvaja]
dhañña: nt.  padi-padian.\n
dhana: nt.  kekayaan, harta, uang.\n
dhanu: nt.  busur.\n
dhanuka: nt.  busur (kecil), busur mainan.\n
dhamana: m.  hal meniup, membunyikan, menyalakan.\n
dhamani: f.  urat nadi; **~santhatagatta**urat nadi di sekujur badan tampak jelas.\n
dhamma: m.  doktrin, ajaran (pl.), kebenaran, legal, norma, hukum (_dhammo sanantano_ kebenaran atau hukum nan abadi), moralitas, kebajikan, sifat intrinsik, kondisi, karakteristik, kualitas (_āyatiṁ anuppādadhammā ti anāgate anuppajanakasabhāvā_), fenomena (_samudaya-dhamma_ yang mengalami kemunculan), objek mental, hal, kewajiban, praktik (jalan hidup), peraturan.   {Menurut Buddhaghosa, dhamma mengandung empat makna yakni _guṇa_ (sifat, kualitas, kebajikan), _desanā_ (ajaran), _pariyatti_ (kitab suci) dan _nissatta_ atau _nijjīva_ (benda, kebenaran, nibbana, eksistensi, dan fenomena juga termasuk di dalamnya.}; **~cakkhu** yang bermata Dhamma, yang telah melihat Dhamma (empat Ariyasacca); **~vāda** teori dhamma; **~sāmin**m.  Wali Dhamma (julukan Sang Buddha). [dharma ← Skt. dharma]
dhammatā: f. sesuai dengan Dhammaniyāma; sesuai, cocok, pantas; aturan umum, hukum, hukum kosmis, kebiasaan, fenomena yang teratur.\n
dhammika: a.  sesuai dengan hukum, sesuai dengan Dhamma atau peraturan, tepat, cocok, benar, diperkenankan, legal, dibolehkan, adil, berbudi, terhormat.\n
dhammiya: a.  sesuai dengan Dhamma, legal.\n
dharati: memegang, membawa, mengenakn, menopang, menahan, bertahan, berlanjut, hidup, ada terus.\n
dhātu: f.  unsur (dasar), elemen; kondisi alamiah, sifat, watak; faktor, pokok, asas, dasar, bentuk, wujud; relik, sisa-sisa jasmani; kasih, suka.\n
dhāreti: (kaus. dari **dharati**)  membawa, menimang, mengenakan, memegang, memiliki, memberikan, memegangkan, menahan, mengingat, menghapal, mencamkan, memahami, mengambil …..sebagai, menganggap …….sebagai, mengakui, membolehkan, menyokong, memberikan, menerima …..sebagai.\n
dhāvati: lari, melarikan diri, berlari, berlari menjauh, memelesat, mengalir; menggelontor, membersihkan (dengan aliran air).\n
dhītar: (**dhītā**) f.  putri.\n
dhītalikā: f.  boneka.\n
dhuta (dhūta) :  (pp dari **dhunāti**)  menggoncangkan, mengiraikan, disingkirkan; penyingkiran kotoran batin.\n
dhutta: a.  liar, bebas, licik, cerdik, curang, culas, jahat, bobrok, bejat, sembrono;  m.  bajingan, bangsat, penipu, penjahat, berandal, pengumbar nafsu, penjangak (orang yang tidak senonoh tingkah lakunya; risau; cabul), bajul (buaya; penjahat, pencuri, pencopet, penggoda perempuan).\n
dhuttikā: f.  **= dhutta**.\n
dhura: m. nt.  kuk, gandar, galah, poros; beban, muatan, tuntutan, tuduhan, jasa, tanggung jawab; bagian depan, kepala, hulu, puncak, seberang; pemimpin, tokoh, penghulu; ujung, bagian puncak atau awal.\n
dhuva: a.  stabil, tetap, permanen, pasti, niscaya; nt. kekekalan, stabilitas; adv. secara tetap, terus menerus, selalu, tentu saja; **~coḷa** selalu tersumbat kain; **~lohita** selalu berdarah.\n
dhūma: m.  asap, kabut.\n
dhūli: f.  debu, duli. [duli ← Skt. dhūli]
dhota: (pp dari **dhāvati**)  telah dicuci, dibilas, dibersihkan.\n
dhovati: mencuci, membilas, membasuh, membersihkan, mengumbah.\n
na: tidak, bukan.\n
nakkhatta: nt.  gugus bintang, rasi, konstelasi; _nakkhattaṁ ādisati_ (atau _oloketi_ atau _uggaṇhāti_) merasi (meramalkan nasib atau jodoh seseorang dengan menilik perhitungan bintang kelahiran).\n
nakha: m. nt.  kuku, cakar.\n
nagara: nt.  kubu, benteng, kota yang diperkuat dengan benteng, kota (termasuk tanah yang berada di seputarnya).\n
nagga: a.  telanjang, bugil.\n
naccaka: m.  penari, aktor (pantomim);  f. **naccakī**.\n
naccati: menari, memainkan (memerankan).\n
naṭṭha: (pp dari **nassati**)  binasa, musnah, hilang, lenyap.\n
nattar: m.  cucu.\n
natthika: a.  yang berpaham “tiada sesuatu pun”, skeptis, nihilis; **~vāda** m.  seorang nihilis.\n
natthu: m.  hidung; = **natthukamma** pengobatan melalui hidung.\n
nadī: f. sungai. [nadi ← Skt. nadī]
nandati: senang, gembira, suka, bangga atas (instr.); kaus. **nandeti**membuat senang, membantu.\n
nandi (nandī): f.  1. _kegembiraan_, kesenangan, kesukaan dalam, gemar; 2. genderang (gendang, tambur) kemenangan.\n
nabha(s): nt.  kabut, awan, langit, angkasa.\n
namakkāra: m.  hal memberi hormat.\n
namati: menekuk, membungkuk, mengarahkan, mengerahkan; kaus. **nameti**menekuk, membentuk.\n
naya: a.  “menuju; jalan, cara, metoda, rencana, gaya, kesimpulan; makna, nuansa; perilaku, sifat, tindak-tanduk; **esa nayo sesesupi** sisanya pun [seyogianya dipahami] dengan cara yang sama.\n
nara: m.  orang, manusia.\n
naraka: m.  ceruk, lubang; neraka. [neraka ← Skt. naraka]
nalāṭikā: f.  kerut (dahi).\n
nahāna: nt.  mandi.\n
naḷeru: m.  nama yaksa.\n
nava: 1.  sembilan; 2.  a. baru, segar, bersih, belakangan, muda, tak berpengalaman (masih hijau), pemula; **~kamma**  nt.  pembangunan baru, pemugaran, perbaikan, renovasi; **~ṅga-buddha-sāsana**sembilan langgam ajaran Sang Buddha yakni _sutta, geyya, veyyākaraṇa, gāthā, udāna, itivuttaka,  jātaka, abbhutadhamma, vedalla_..\n
navanīta (nonīta): nt.  mentega segar, nawanita (gumpalan hasil pengadukan dadih yang kebanyakan terdiri dari lemak susu dan padatan susu).\n
navama: kesembilan, ke-9, IX.\n
nassati: binasa, musnah, hilang, lenyap, lesap, berakhir, hancur, rusak.\n
nahāpita: m.  tukang cukur yang juga memberi layanan mandi (salah satu golongan yang tingkat sosialnya dianggap rendah).\n
nahāyati (nhāyati): mandi, mencuci, melakukan pembersihan diri (terutama saat berakhirnya kecantrikan keagamaan atau setelah berakhirnya masa penyucian diri).\n
nāga: m.  1.  naga; gajah (terutama yang kuat dan milik negara, simbol kekuatan dan ketahanan); hewan; pahlawan atau orang suci; 2. nagasari (Skt. _nāgakeśara_; _Mesua ferrea_);  **hattha~** gajah Nāga.\n
nātha: m.  pelindung, pengayom, protektor, penolong, penyelamat.\n
nānā: adv. berbagai macam, aneka jenis, majemuk, macam-macam, aneka, segala macam, beragam, berbeda(-beda), terpisah.\n
nābhi (nābhī): f.  pusat, pusar; poros (roda).\n
nāma: nt.  nama, julukan, panggilan; batin; kata benda; **~vibhatti**f.  deklensi kata benda; _nāmaṁ karoti_ menamakan, menjuluki. [nama ← Skt. nāma]
nāmaka: a.  bernama, dengan nama, diberi nama; dengan nama belaka, omongan belaka, omong kosong, menggelikan.\n
nāyaka: m.  pemimpin, ketua, wali. [nayaka ← Skt. nāyaka]
nārī: f.  perempuan, wanita.\n
nāla (nāḷa): nt. tangkai hampa (terutama seperti tangkai kangkung).\n
nāḷikera: m.  pohon kelapa; kelapa.\n
nāvā: f.  perahu, kapal.\n
nāvika: m.  pelaut, kelasi, anak kapal; nakhoda kapal; tukang tambang.\n
nāsaka: m.  pembinasa, penghancur, pemusnah.\n
nāsana: nt.  kebinasaan; hal ditinggalkan atau diusir; **~antika**a. yang berada di bawah hukuman pengusiran; (Menurut V.A. 428 ada tiga jenis: _saṁvāsa_, _liṅga_, dan _daṇḍakamma_).\n
nāsika: a.  milik hidung; **~sota**m. nt.  lubang hidung.\n
nāseti: menghancurkan, merusak, membinasakan, memusnahkan, membunuh; bertobat; mengusir.\n
nikati: f.  penipuan, kecurangan, kebohongan, ketidakjujuran; instr. _nikatiyā_, _nikatyā_, _nikacca_.\n
nikāya: m.  kumpulan, gerombolan, kelompok, golongan, dunia, alam; kumpulan sutta.\n
niketa: m.  rumah, kediaman, mukim, persinggahan; rombongan, peguyuban, kelompok.\n
nikkaṅkha: a.  tidak ragu.\n
nikkama: a. m. upaya, kekuatan, ketahanan, ketekunan, keuletan, ikhtiar.\n
nikkujjita: pp dari **nikkujjati**) tertelungkup, terjungkir balik.\n
nikkhamati: pergi dari, keluar dari, keluar, pergi keluar, berangkat pergi, beranjak pergi, pergi meninggalkan, tinggal pergi, meninggalkan, keluar menuju, berpaling dari.\n
nikkhameti (nikkhāmeti):  (kaus. dari **nikkhamati**) mengeluarkan, membawa keluar, membawa pergi.\n
nikkhitta: (pp dari **nikkhipati**)  diletakkan, terletak, diletakkan ke dalam, dipasang, disusun; menjauhi atau bebas dari.\n
nikkhipati: meletakkan (dengan hati-hati), menyimpan, menyisihkan, menyingkirkan, mengenyahkan, mencampakkan.\n
nikkhepa: m.  hal meletakkan, menggeletakkan, membuang, mencampakkan, menyisihkan, menyingkirkan, melepaskan, menolak; ringkasan, rangkuman, ikhtisar.\n
nikhanati (nikhaṇati): menggali, menimbun, menegakkan, menutupi (menimbuni), membenamkan; **akkhiṁ ~** mengedipkan mata.\n
nikhāta: (pp dari **nikhaṇati**) digali, ditanam atau ditimbun, dibenamkan, ditegakkan, ditancapkan, dihunjamkan, dipancangkan.\n
nikhādana: nt.  “makan ke dalam”, alat tajam, sekop atau pahat.\n
nigacchati: turun menuju, memasuki, menuju, menderita.\n
nigama: m.  kota (kecil), kota niaga (biasanya di tepi sungai), bandar.\n
niggaṇhāti: menahan, mengendalikan; memarahi, mengecam.\n
niggaha: m.  pengendalian, kontrol, pengekangan, penahanan; comelan, celaan, kecaman, hal menyalahkan; sangkalan, pembuktian kesalahan, penyidangan.\n
nigghosa: m.  seruan, ungkapan, ucapan; reputasi, kemasyhuran; celaan, teguran.\n
nicca: a.  tetap, kekal, langgeng, abadi, terus menerus, reguler;  nt. adv  **niccaṁ** secara terus menerus, selalu, senantiasa.\n
niccala: a.  diam tidak bergerak, bergeming.\n
niccharati: pergi menuju, muncul, keluar dari; kaus. mengeluarkan, melepaskan, melontarkan, mengutarakan.\n
nija: a.  milik diri sendiri; **~desa**m.  negeri sendiri.\n
nijjhāyati: merenungkan, hanyut dalam.\n
niṭṭhāna: nt.  diselesaikan, dibereskan, dituntaskan, dilaksanakan, dilakukan, dikerjakan.\n
niṭṭhita: a.  berakhir, selesai, siap; disiapkan, tamat, habis.\n
niṭṭhubhati (nuṭṭhubhati, niṭṭhuhati): meludah.\n
nittharati: menyeberangi, melampaui, mengatasi, meninggalkan, terbebas dari; pp. **nitiṇṇa**; kaus. **nitthāreti** mengatasi
nidassana: nt.  “menunjuk pada; kenyataan, contoh, tampak, wujud penampakan, pembandingan, keterangan tambahan, atribut, ciri, sifat, tanda, label, embel-embel.\n
nidahati: meletakkan, menimbun, menguburkan, menyembunyikan (dalam tanah), menyimpan.\n
nidāna: nt.  dasar, landasan, sumber, asal muasal, sebab, alasan, rujukan, subjek, (bagian) pengantar; **tatonidānaṁ**dengan ini, oleh ini, gara-gara ini, lantaran.\n
niddā: f.  tidur; **~ārāma(na)** gemar tidur. [nidera ← Skt. nidrā]
niddiṭṭha: (pp dari **niddisati**) terungkap, dijelaskan, ditunjukkan, dipaparkan, diungkapkan, didefinisikan.\n
niddisati: menjelaskan, menguraikan, menunjukkan, mendefinisikan, mengungkapkan, memaparkan, berarti.\n
niddesa: m. illustrasi, penjelasan, uraian, analisis, penggambaran, hal melukiskan, petunjuk.\n
nidhāna: nt.  hal menyimpan, mengamankan, menaruh, menempatkan, menabung, mencadangkan, membekam, memendam, memeram, menyembunyikan, menanam; harta (karun), penyimpanan, tabungan, wadah penyimpan.\n
nidhi: m.  1. yang ditimbun atau dibenamkan dalam tanah, harta yang disembunyikan; 2. hal mengenakan (mantel).\n
nindati: menyalahkan, mencela, mengecam, menghina.\n
nindā: f.  hal menyalahkan, mencela, mengecam, menghina.\n
ninna: a.  melengkung ke bawah; rendah, dalam, cekung; condong pada, cenderung pada, mengarah pada, menuju ke; ke bawah; nt. dataran rendah, lembah, tanah rendah, lembang.\n
ninnāmin: a.  turun, menurun.\n
nipaka: a. cerdik, cerdas, pandai, cermat, bijaksana.\n
nipajjati: berbaring; kaus. **nipajjāpeti**membaringkan, meletakkan, menyimpan.\n
nipanna: (pp dari **nipajjati**) berbaring.\n
nipāta: m.  jatuh, turun; partikel (kata yang biasanya tak dapat diderivasikan atau diinfleksikan, mengandung makna gramatikal dan tidak mengandung makna leksikal, termasuk di dalamnya artikel, preposisi, konjungsi, interjeksi, dan kata keterangan); bagian buku, bab.\n
nipāteti: membuat jatuh, menjatuhkan, melempar, melukai, mencampakkan, membaringkan.\n
nippīḷana: nt.  hal memencet, menekan, memeras; pukulan.\n
nippīḷeti: memeras, menekan, memencet, mencengkeram, mendesak.\n
nipphanna: (pp dari **nippajjati**)  tercapai, berhasil, sempurna, terlatih, terwujud, terbentuk.\n
nibbattati: keluar dari muncul, menjadi, dihasilkan, dilahirkan, terlahir, timbul.\n
nibbattana: nt.  tumbuh, mengemuka, muncul, lahir, eksist, hidup.\n
nibbatteti: (kaus. dari **nibbattati**) menghasilkan, melahirkan, menimbulkan, menerbitkan; melakukan; mengamalkan, menemukan.\n
nibbāti: mendingin, menjadi tidak bernafsu.\n
nibbāna: nt.  kepadaman, kesegaran, kebugaran, kelenyapan keserakahan kebencian dan kegelapan batin, nirwana, pemadaman total; (Udāna 8.3/80 _ajātaṁ abhūtaṁ akataṁ asaṅkhataṁ_).  [_nibbāna_ merujuk ke keadaan, sedangkan _parinibbāna_ merujuk ke pencapaian keadaan tsb.] [nirwana ← Skt. nirvāṇa]
nibbāyati: mendingin, menjadi segar, padam, lenyap.\n
nibbāhati: membawa keluar, mengeluarkan, memindahkan; **nibbāhāpeti**menyuruh membawa keluar, membongkar muatan, mengangkut pergi.\n
nibbāhana: a. menuntun keluar, mengenyahkan, menyelamatkan; nt. pengenyahan, pembersihan, perlindungan, jalan keluar.\n
nibbidā: f. kejemuan, kebosanan, keengganan, ketidakpedulian, kekecewaan, kecuekan, kemasabodohan, ketidakacuhan, kejijikan, kejenuhan, muak terhadap kehidupan duniawi.\n
nibbindati: jemu, bosan, muak, kecewa, enggan.\n
nibbeṭhita: (pp dari **nibbeṭheti**) dijelaskan, tersingkap, diperjelas.\n
nibbeṭheti: mengurai kekusutan, melepas lilitan, menjelaskan, menyingkapkan, menjernihkan; menyangkal, menolak; berkelit, mengelik, mengelak.\n
nibbhujjhati: beradu gulat, bergulat.\n
nibbhoga: a.  tidak berguna, yang telah dicampakkan atau ditinggalkan, tidak mengenal penikmatan, bukan seorang penikmat.\n
nimanteti: mengundang, mempersilakan.\n
nimitta: nt.  tanda, isyarat, alamat, pertanda, tengara, gelagat; ciri, penampakan, sifat, karakteristik, atribut, corak, fenomena; bayangan atau gambaran dalam batin; tanda sasaran; alat kelamin; dasar, alasan, kondisi; **~kamma**nt. (pe)ramalan, (pe)nujuman.\n
nimugga: a.  dicemplung ke dalam, direndam dalam, dipendam dalam, dibenam.\n
nimujjati: tenggelam, cemplung ke dalam, menyelam ke dalam, terjun ke dalam, terendam dalam
nimmadana: nt.  penyentuhan, sentuhan, penghancuran, pengikisan, penundukan, menghilangkan kemabukan (keangkuhan).\n
niyata: a.  terkendali, terikat pada, terkungkung dalam, niscaya, pasti, tentu, perlu.\n
niyama (niyāma): 1. pengendalian, latihan, keterkendalian, keterbatasan; keniscayaan, keteraturan, ketentuan, kepastian, batasan; hukum alam, keteraturan kosmis; **niyamena** (**niyamato**)  adv.  harus, perlu; 2. cara, jalan, metoda, praktik.\n
niyyati (nīyati): dibimbing, dituntun, pergi, dipindahkan.\n
niratta: a.  yang tidak/belum diasumsikan atau diterima (dianggap), yang telah dicampakkan atau ditolak.\n
nirabbuda: a. bebas dari bisul atau tumor, sehat; bebas dari kebobrokan.\n
niraya: neraka, alam penuh siksaan.\n
nirādīnava: a.  tidak dalam ancaman bahaya.\n
nirujjhati: (pass. dari **nirundhati**) dihancurkan, dileburkan, diluluhkan, berakhir, berhenti, lenyap, meninggal.\n
nirutti: f.  salah satu dari enam _Vedāṅga_ (_kappa,_ _vyākaraṇā, nirutti, sikkhā, chando/ viciti, jotisattha_); penjelasan kata-kata, analisis tata bahasa, tafsiran etimologis, tafsiran turunan kata, pelafalan, pengucapan, ucapan, dialek, cara berbicara, gaya bahasa, (peng)ungkapan, ekspresi.\n
niruddha: (pp dari **nirundhati**)  dienyahkan, dihancurkan, diakhiri, dihentikan, dilenyapkan, terintang.\n
nirodha: m.  kehancuran, keleburan, keluluhan, keberakhiran, kelenyapan, _hal berhenti_.\n
nilīna: (pp dari **nilāyati**)  duduk di atas, menduduki, bertengger di atas, bersembunyi, mengendap (menunggui).\n
nilīyati: berjongkok (terutama dengan tujuan bersembunyi); mengendap(-endap); bersembunyi.\n
nivattati: berbalik, berputar balik, berpaling dari; lolos, hilang, lenyap, gaib, musnah, pupus, sirna, kabur, berhenti, berakhir.\n
nivattana: nt. putaran, balikan, belokan, hal berpaling dari, berbelok, melepaskan, berbalik arah (konversi); membelot; kelok, lengkung, tikungan, keluk.\n
nivasati: tinggal, berdiam, hidup, menetap.\n
nivāta: a.  “dengan angin mengalir ke bawah”, tanpa angin, terlindung dari angin, terlindung, aman; nt. tenang; m. kerendahan, kerendahan hati, kepatuhan, kesantunan.\n
nivāpa: m.  makanan yang dilemparkan atau ditaburkan, rangsum, makanan hewan.\n
nivāraṇa: a. nt.  penahan, perintang, pencegah, penangkal.\n
nivāreti: (kaus. dari **nivarati**)  menahan, menghentikan, melarang, menolak.\n
nivāseti: mengenakan pakaian, mengenakan jubah bawah.\n
niviṭṭha: (pp dari **nivisati**)  didiami, didirikan, dibangun, dikukuhkan, pasti; ditambatkan pada, cenderung, bertekad, condong pada.\n
nivisati: memasuki, berhenti, berdiam di, mengambil jalan, menetap di.\n
nivesana: nt.  hal memasuki, pintu masuk, hunian, penghunia, kediaman, rumah (umat awam), panti, hal mendiami, kemelekatan.\n
nisajjā: f.  duduk, kesempatan untuk duduk, tempat duduk.\n
nisanti: f.  perhatian atau pengamatan yang cermat, pencerapan
nisādin: a.  berbaring.\n
nisāmeti: memperhatikan, menyimak, mengamati, mencermati, mengindahkan, hati-hati, mencerap.\n
nisinna: (pp dari **nisīdati**)  duduk.\n
nisīdati: duduk.\n
nisīdana: nt.  kain duduk.\n
nissaṁsaya: a.  tiada ragu, tiada sangsi, tak diragukan lagi, tak pelak lagi, tak syak lagi.\n
nissaggiya: a.  yang harus dilepasserahkan; benda yang dilepasserahkan, yang dilontarkan.\n
nissajjati: membebaskan, memberikan, melepaskan, menyerahkan, menuangkan.\n
nissaṭṭha: (pp dari **nissajjati**)  dibebaskan, dilepaskan, ditinggalkan, diberikan, diserahkan.\n
nissayati: bersandar pada, berlandaskan, bergantung pada, mempercayai, mengikuti.\n
nissaraṇa: nt.  keluar, meninggalkan; keluaran, hasil, menanggalkan, terbebas, pembebasan.\n
nissāya: ger. dari **nissayati**) menyandar pada; dekat, hampir, di atas; melalui, dengan cara, dengan bersandar pada, dikarenakan, atas dukungan atau lindungan; sebab, karena, demi.\n
nissita: (pp dari **nissayati**)  bergantung pada, menghuni, menempel pada, ditopang oleh, hidup bersandar pada, bersandar pada, beralaskan, berlandaskan, condong pada; lahan.\n
nisseṇi: f.  tangga, tangga pemanjat, senigai.\n
nīta: (pp dari **neti**)  dituntun, dibimbing, dipastikan, dianggap, diduga, disimpulkan, dibawa pergi, diculik.\n
nīla: a.  biru tua, biru gelap, biru kehijau-hijauan, hijau kebiruan; warna gelap. [nila ← Skt. nīla]
nīlaka: a.  ▶ **nīla**
nīvaraṇa: nt. m.  rintangan, halangan, hambatan.\n
nīvārā: m.  padi (liar).\n
nīhāraka: a. m.  seseorang yang membawa pergi, seseorang yang mengantarkan.\n
nīharati: mengeluarkan, melontarkan, mencampakkan, menembusi, menghantarkan.\n
nu: (partikel penegas); partikel pertanyaan (interogatif); **na nu** tidakkah.\n
nūna: apakah lalu, sekarang, akankah; tentu saja; **yaṁ nūna**bagaimana kalau, akankah saya, biar saya.\n
nekkhamma: nt.  hal meninggalkan kesenangan duniawi, meninggalkan kesenangan nafsu indriawi. (_kāmānaṁ nissaraṇaṁ yad idaṁ nekkhammaṁ_)
negama: a. penghuni atau penduduk kota (kecil) atau bandar, orang-orang.\n
neti (nayati): menuntun, membimbing, bertindak, mengambil, membawa (pergi), menggiring, menyimpulkan, memahami, menganggap; pass. **nīyati**, **niyyati**.\n
netthar: m.  **netthāraṁ vattati** berperilaku sedemikian rupa sehingga bebas cela, berperilaku korek.\n
nerayika: a.  berhubungan dengan alam neraka; yang akan menderita di alam neraka.\n
no: 1.tidak, bukan; tentu saja tidak/bukan; **no ca** cuma belum, hanya saja tidak; **no ca kho** namun tentu saja bukan/tidak;**no na** sama sekali tidak/bukan; **no hi taṁ**tentu saja bukan demikian; 2.bentuk enklitik dari gen. dat. akk. dari pronomina orang pertama jamak (=**amhākaṁ**); 3. = **nu**.\n
paṁsu: m.  debu, kotoran, duli, tanah; **~kūla**benda (misalnya kain) usang dari tumpukan sampah, kain usang, barang buangan; **~kūlika** orang yang mengenakan pakaian yang terbuat dari kain usang tumpukan sampah.\n
pakata: a.  yang sudah dilakukan, dibuat; bersifat, dilanda, dihinggapi, dipengaruhi.\n
pakati: f.  wujud asli (asal) atau alami, keadaan (sifat) alami; asli, utama; kesempatan, kejadian, peristiwa; **pakatiyā** sebenarnya, biasanya, lazimnya, sebagaimana biasanya, dengan sendirinya, secara otomatis. [pekerti ← Skt. prakṛti]
pakaraṇa: nt.  perbuatan, perkara; kesempatan, peristiwa, kejadian, alasan; eksposisi, aransemen, karya sastra, komposisi, buku. [perkara ← Skt. prakaraṇa]
pakāra: m. bahan penyusun, bahan pembangun, bahan perlengkapan; susunan, persiapan, mode (modus), cara, aspek, seluk-beluk; bahan ramuan; jenis.\n
pakāsati: memancarkan, memaklumkan.\n
pakāseti: (kaus. dari **pakāsati**)  menunjukkan, memperlihatkan (_agāravaṁ pakāseti_), menjelaskan, memaklumkan, mengulas.\n
pakiṇṇaka: a.  yang bertaburan [di sana-sini], yang sesekali ada di; aneka macam, khusus, khas, tertentu; **~kathā**aneka bahasan.\n
pakka: a.  matang, masak; sudah dimasak, direbus, dipanggang, ranum, bonyok, rusak, membusuk; panas, berpijar; nt. buah, buah matang.\n
pakkamati: berjalan maju, pergi meninggalkan, berangkat pergi, beranjak pergi.\n
pakkosati: memanggil, menyerukan; kaus. **pakkosāpeti**.\n
pakkha: 1. m.  sisi (badan), sayap, kepak; pihak, bagian, faksi, kelompok, pengikut, partisan, sekutu; paruh(-an) (bulan) (_sukka-pakkha_ atau _juṇha-pakkha_  paruh terang; _kāḷa-pakkha_ atau _kaṇha-pakkha_  paruh gelap); alternatif, pernyataan, sehubungan dengan merujuk pada; **~jāta**m.  yang bersayap, unggas; 2. a.  tampak, jelas, seperti, mirip; 3. m.  orang pincang. [paksa ← Skt. pakṣa]
pakkhaka (pakkhika) :  busana yang terbuat dari (bulu) sayap (burung).\n
pakkhandati: memelesat, melontar ke depan, melompat ke.\n
pakkhāleti: mencuci, membasuh, membilas.\n
pakkhika: a.  berkaitan atau merujuk ke paruhan bulan; penopang menuju
pakkhitta: (pp dari **pakkhipati**) diletakkan di dalam, dilontarkan ke dalam.\n
pakkhipati: meletakkan di dalam, menempatkan di dalam, memasukkan ke dalam, melontarkan ke dalam; meliputi, menyisipkan, menyusun.\n
pageva: adv.  apalagi.\n
paggaṇhāti: merentangkan, menjangkau, memegang, menghadang, mengulurkan, mengangkat, mengambil; menerima, menjaga, mengurus, menyokong, melindungi, merawat, menolong; mengerahkan, mengupayakan, berikhtiar, berupaya, menerapkan, berjuang, bersikeras; _añjaliṁ ~_ mengangkat sembah.\n
paggaha (paggāha): m.  usaha, upaya, pengerahan tenaga, daya, kekuatan,perjuangan; kemurahan hati, kebaikan hati, (per)lindungan.\n
paggharati: mengalir (keluar), mengeluarkan (darah), menetes, merembes.\n
paṅgacīra: nt.  meniup seruling daun.\n
pacati: memasak, merebus, memanggang; menyiksa; pass. **pacīyati**, **paccati**.\n
pacalāyati: berkedip, berkejap, mengantuk, meralip (amat mengantuk, setengah tidur), luyu, ruyup (berasa ngantuk atau tampak sangat mengantuk).\n
pacāreti: menangani, mempublikasikan, menyiarkan, mengunjungi.\n
paccakkha: a.  “di depan mata”, dapat dicerap indra, nyata, jelas, ada; **paccakkhena** secara pribadi; **paccakkhato**  dari pengalaman pribadi; **appaccakkhāya**  tanpa melihat atau mengarahkan persepsi (pencerapan); memungkiri, mengingkari.\n
paccakkhāti: mengingkari, memungkiri, menolak, melepaskan.\n
paccati: (pass dari **pacati**)  direbus, dimasak, disiksa, menderita.\n
paccatta: a.  secara terpisah atau individu, sendiri-sendiri, masing-masing, oleh diri sendiri; adv. **paccattaṁ**.\n
paccattharaṇa: nt. kain penutup, seprai ranjang atau kursi.\n
paccatthika: a.  lawan, musuh, seteru.\n
paccaya: m.  hal bersandar pada, dasar, sarana, penopang, sara hidup, kondisi, sebab musabab, _alasan_, landasan untuk; kebutuhan; kepercayaan, keyakinan.\n
paccāgacchati: kembali, kembali lagi, balik kembali, menarik diri, mundur dari; **sārato ~** menganggap … sebagai faktor penentu.\n
paccāsati: memohon, meminta, mendoakan.\n
paccāsiṁsāti: mengharapkan, mendambakan, menginginkan, memohon, mengharapkan ganjaran atau imbalan.\n
paccāharati: membawa kembali.\n
paccuṭṭhāti: berdiri, muncul kembali, berdiri menyambut.\n
paccupaṭṭhahati: “berdiri di hadapan”, hadir.\n
paccupaṭṭhāna: nt.  penampilan, manifestasi, kemunculan, pemunculan, fenomena; perawatan.\n
paccupaṭṭhita: (pp dari **paccupaṭṭhahati**) dikedepankan, disajikan, ditawarkan, diajukan, diberikan, dekat, siap(-sedia), hadir, ada.\n
pacceka: a.  masing-masing, satu, (berdiri) sendiri, tunggal, sendirian, terpisah, aneka; **paccekaṁ**adv.\n
pacceti: tiba pada, kembali ke, bersandar pada, memahami (melihat) sebagai, berpandangan.\n
pacchā: adv.  di belakang, setelah, sebelah barat; **~samaṇa** petapa atau bhikkhu yunior yang berjalan di belakang seorang senior dalam suatu perjalanan (sebagai pendamping atau pelayan); **~bhatta**usai makan. [pasca ← Skt. paṡcā]
pacchijjati: terputus, terpotong.\n
pacchima: a.  yang terbelakang, terakhir, terbuncit, belakangan, di belakang hari; terendah; barat.\n
pacchimaka: a.  yang terakhir, yang terendah, yang paling buncit, yang paling terbelakang.\n
pajahati: meninggalkan, menanggalkan, mengenyahkan, menyingkirkan; pass. **pahīyati**.\n
pajā: f.  keturunan, anak cucu; penghuni (dunia), makhluk hidup, orang, umat manusia. [praja ← Skt. prajā]
pajānāti: mengetahui (secara jelas dan mendalam), menemukan, menyelami, memahami.\n
pajāpati: m.  kepala atau pemimpin tertinggi umat manusia;  f.  “seseorang yang memiliki keturunan”; permaisuri, istri.\n
pajāpatī (pajāpati): f.  Pencipta (Tuhan) semua makhluk hidup; memiliki keturunan, beranak cucu (banyak), permaisuri, istri utama, istri, nyonya.\n
pajjalati: terbakar, tersulut, membara.\n
pajjota: m.  cahaya, kecemerlangan, lampu, pelita.\n
pajjhāyati: terbakar, rusak binasa, melapuk, mengering, lesu, lunglai; hanyut dalam kesedihan, kekecewaan, atau penyesalan; murung, termenung, _termangu_; **pajjhāyanto**sedih, susah, putus asa.\n
pañca: a.  lima.\n
pañcama: a.  kelima, ke-5, V.\n
paññatta: (pp dari **paññāpeti**) ditunjukkan, dimaklumkan, disuruh, dirancang, ditetapkan, ditunjuk, ditahbiskan, dinobatkan, disiapkan, disediakan.\n
paññā: f.  pengetahuan atau pemahaman yang mendalam, kebijaksanaan.\n
paññāpeti: memaklumkan, menunjukkan, menunjuk, menempatkan, menetapkan, menentukan; meletakkan, menggelar, memaparkan, menyiapkan, menyediakan.\n
pañha: m.  cara bertanya, penyeledikan, pertanyaan; **~vyākaraṇa** cara menjawab pertanyaan (ada empat yakni _ekaṁsa_, _vibhajja_, _paṭipucchā_, dan _ṭhapanīya_ D iii 229; A i 197 sq; ii 46; Miln 339).\n
paṭa: m.  kain, jubah, pakaian.\n
paṭikacca: sebelumnya, mempersiapkan; mewanti-wanti (**paṭigacca**).\n
paṭikaḍḍhanā: f.  hal mendorong.\n
paṭikassati: menarik kembali, mencabut (kembali), melontarkan kembali, mengirim kembali, menyeret kembali.\n
paṭikuṭṭha: a.  dimarahi, ditegur, diomeli, dicela, rendah, hina, dipandang rendah.\n
paṭikkanta: (pp dari **paṭikkamati**) pulang dari, kembali dari, mundur.\n
paṭikkamati: balik, kembali, mundur.\n
paṭikkamana: nt.  kembali, mundur, balik kembali.\n
paṭikkūla: a.  berlawanan, menjijikkan; nt. hal menjijikkan.\n
paṭikkhitta: (pp dari **paṭikkhipati**)  yang ditolak, yang dilarang.\n
paṭigaṇhāti: menyetujui.\n
paṭiggaṇhāti (paṭigaṇhāti): menerima, mencerap, menanggap, mengambil; kaus. **paṭiggaheti**.\n
paṭigha: m. nt.  resistansi, hal menangkal, menolak, menentang, menghalau; tak suka, teriritasi, perasaan sebal, marah. (=**aniṭṭhaṁ**).\n
paṭighāta: m.  menangkal, menangkis, mencegah.\n
paṭicaya (paṭiccaya): m.  penambahan, penumpukan, pengumpulan.\n
paṭicca: berdasarkan, dikarenakan, sehubungan dengan, sebab, terkondisi oleh.\n
paṭicchanna: (pp dari **paṭicchādeti**) tertutup, terselubung, tersembunyi, _tersekat_, _terpencil_.\n
paṭicchādeti: menutupi, menyelubungi.\n
paṭijānāti: mengakui, mengatakan, menyetujui, memaklumkan, menjanjikan, berjanji.\n
paṭiñña: a.  dimaklumkan, membuat percaya, palsu, pura-pura, berlagak seperti; memperkenalkan diri sebagai.\n
paṭiññā: f.  pemakluman, kesepakatan, perjanjian, persetujuan, izin.\n
paṭiññāta: (pp dari **paṭijānāti**)  disetujui, diakui, dijanjikan.\n
paṭinivattati: kembali lagi, balik kembali.\n
paṭinissagga: m.  pelepasan, penanggalan, penolakan.\n
paṭinissajjati: menyerahkan, melepaskan.\n
paṭinissaṭṭha: (pp dari **paṭinissajjati**)  dilepaskan, diserahkan.\n
paṭipajjati: menapaki, menyusuri, mengikuti, menjalani, menyusul; mengambil suatu rangkaian tindakan, mengikuti suatu metoda; berniat untuk, mengatur kehidupan sendiri.\n
paṭipaṇāmanā: f.  hal menyorong.\n
paṭipatti: f.  “jalan”, cara, metoda, tindak-tanduk, praktik, pengamalan, perilaku, contoh (teladan).\n
paṭipatha: m.  jalan berlawanan (arah); _paṭipathaṁ gacchati_  berpapasan.\n
paṭipadā: f.  jalan untuk mencapai suatu tujuan; jalan, cara, praktik, tata cara menuju.\n
paṭipanna: (pp dari **paṭipajjati**) (telah) diikuti atau mengikuti, mencapai, menapaki, menyusuri, berperilaku, bertindak, memasuki, memperoleh, meraih.\n
paṭipādeti: (kaus. dari **paṭipajjati**) memberi, membuat menjadi, menawarkan, menghadiahkan.\n
paṭipuggala: m.  orang sepantar/sebanjar, individu pengimbang, lawan, rival; **apaṭipuggala**a.  tanpa lawan, tiada bandingan.\n
paṭipuggalika: a.  yang sepantar/sebanjar, secara individu.\n
paṭipucchati: balik bertanya, menanyakan, mempertanyakan.\n
paṭippassambhati: surut, mereda, menjadi tenang, hilang, terhapus, batal, teranulir.\n
paṭibaddha: a.  terikat pada, terbelenggu, terpikat pada, bergantung pada, menempel pada.\n
paṭibala: a.  mampu, pantas, kompeten, cakap.\n
paṭibujjhati: sadar, bangun, paham, mengetahui.\n
paṭibuddha: (pp dari **paṭibujjhati**) sadar, terjaga.\n
paṭibhāna: nt.  pemahaman, penerangan, kecerdasan, inteligensi, kemahiran atau kecakapan berbicara, ketangkasan, kecerdikan.\n
paṭimāneti: menunggu, menunggui, menjaga, menghormati, melayani.\n
paṭimuñcati: menambat, mengikat, membelit, mengelat, membebat, menyangkut.\n
paṭiyādeti: menyiapkan, menyediakan, mengatur, memberi, mempersembahkan; kaus. **paṭiyādāpeti** menyuruh menyajikan atau menyiapkan, memberikan, menetapkan, menasihati.\n
paṭirūpa: a.  cocok, pantas, sesuai, serasi; dengan urutan yang tepat, disesuaikan terhadap.\n
paṭilabhati: memperoleh, menerima, mendapat.\n
paṭivattiya: a.  diputar balik, digelinding balik, dihentikan penggelindingannya.\n
paṭiviṁsa (paṭivisa): m.  bagian, porsi, jatah.\n
paṭivijānāti: mengenali, memahami; menangkap (maksudnya).\n
paṭivijjhati: menembusi, menerobosi, menembusi (mengetahui) secara batiniah, menguasai, memahami.\n
paṭivinaya: m.  penaklukan, penundukan, penanggulangan.\n
paṭivinodeti: menyingkirkan, menanggalkan, meninggalkan, mengusir, membebaskan diri dari.\n
paṭivirata: (pp dari **paṭiviramati**)  menjauhi, menghindar dari.\n
paṭiviramati: menjauhi, menghindari.\n
paṭivutta: 1. dibalas, dijawab, disahut; 2. disemai (ditanam) kembali.\n
paṭivedha: m.  hal menembusi, penembusan, pemahaman, pencapaian, pengetahuan.\n
paṭisaṁyujati: berhubungan dengan, berkaitan dengan; mulai, melibatkan diri.\n
paṭisaṁyutta: (pp dari **paṭisaṁyujati**)  berhubungan dengan, berkaitan dengan, terlibat
paṭisaṁvedeti: mengalami, merasakan, menjalani, mencerap, menyadari.\n
paṭisaṅkhārika: a.  dicadangkan atau digunakan untuk perbaikan.\n
paṭisandhi: m.  penyambungan kembali, penyambung, penyambungan kesadaran.\n
paṭisambhidā: f.  analisis, pengetahuan analitik yakni _attha_, _dhamma_, _nirutti_ dan _paṭibhāna_; nama lain dari _Paṭisambhidāmagga_, salah satu kitab dari kumpulan kitab _Khuddakanikāya_.\n
paṭisammodeti: balik memberi salam.\n
paṭisallāna: nt.  penyendirian untuk bermeditasi, penyendirian, pengucilan diri, pemencilan diri.\n
paṭisalliyati: menyendiri, menyepi, mengucilkan diri (untuk bermeditasi).\n
paṭisallīna: (pp dari **paṭisalliyati**)  menyendiri, pergi menyendiri, memisahkan diri, tenggelam dalam meditasi.\n
paṭisāmeti: merapikan, menyusun, menyiapkan, membenahi, menyimpan.\n
paṭisevati: mengikuti, menapaki, memperturutkan hati, melakukan, mempraktikkan.\n
paṭisevana: nt.  mengikuti, terlibat dalam, hanyut dalam, praktik, penggunaan secara benar.\n
paṭisotaṁ: adv.  menentang arus.\n
paṭissuṇāti: menyahut, menjawab, menyetujui, menjanjikan, mengiyakan.\n
paṭola: m.  petola, ketola (manis) (PED: _Trichosanthes dioeca_; KBBI: _Luffa cylindrica_); ketola ular (_Trichosanthes anguina_). [petola ← Skt. paṭola]
paṭṭhahati: menurunkan, meletakkan, menyediakan; kaus. **paṭṭhapeti** menyediakan, memberikan, mengeluarkan, menawarkan, mendirikan, membangun.\n
paṭṭhāna: nt.  penegakan, landasan, tumpuan.\n
paṭṭhāya: meletakkan, mulai dari, sejak.\n
paṭhama: a.  pertama, sulung, terdahulu, terkemuka; **~tara**adv. yang pertama, yang pertama-tama, pada awalnya. [pertama ← Skt. prathama]
paṭhavī: f.  bumi, tanah, lantai. [pertiwi ← Skt. pṛthivī]
paṇaka (paṇṇaka): m.  1. dedaunan hijau, sayur-sayuran; 2. nama sejenis tanaman air; 3. daun yang ditulisi, tiket.\n
paṇamati: membungkuk, menekuk; bungkuk; condong terhadap; kaus. **paṇāmeti** membungkukkan, memberi hormat; menekuk, menutup; menyuruh pergi, menolak.\n
paṇidahati: mengusahakan, mengupayakan, menimpakan, mengerahkan, menerapkan, mengarahkan, bermaksud untuk, berhasrat, bercita-cita, mengharapkan, berikrar, mendoakan, merindukan, menginginkan, mendambakan; ger. **panidhāya**.\n
paṇidhi: f.  cita-cita, harapan, dambaan, doa, ikrar, niat.\n
paṇīta: (pp dari **paneti**) a. yang dikenakan, yang diterapkan, yang dikemukakan; unggul, enak, agung, tinggi, luhur, melimpah, mewah, bagus.\n
paṇḍaka: m.  orang kasim.\n
paṇḍita: a.  bijaksana, bijak, pandai, cakap, piawai, cermat, cendekia. [pendeta ← Skt. paṇḍita]
paṇḍu: a.  merah atau kuning muda (pucat), kemerah-merahan, abu-abu;  **~palāsa** daun layu.\n
paṇṇa: nt.  daun (terutama daun sirih); ada lima jenis daun yang dianjurkan untuk dipergunakan sebagai obat (_nimba_, _kuṭaja_, _paṭola_, _sulasi_, dan _kappāsika_); daun untuk menuliskan huruf, daun bertulisan, surat; sumbangan, derma, warisan, pusaka, pesan; bulu sayap, sayap.\n
paṇṇāsā (paññāsā): f.  lima puluh.\n
patati: jatuh, lompat, menimpa, turun.\n
patana: a. jatuh, runtuh; nt. hal jatuh, runtuh, mendarat.\n
pati: m.  tuan, juragan, majikan, pemilik, pemimpin, pamong, kepala, penghulu, tokoh; suami, kepala rumah tangga, umat awam. [patih ← Skt. pati]
patika: a.  bersuami.\n
patita: (pp dari **patati**) jatuh.\n
patiṭṭhahati (patiṭṭhāti)  : berdiri kokoh, mencari dukungan dalam, ditegakkan, dimantapkan, dikukuhkan, ditetapkan, disusun; mengakui; kaus. **patiṭṭhāpeti** mendirikan, membangun, memasang.\n
patiṭṭhāna: nt.  hal menambatkan, memasang, penopang, pembantu, landasan, dasar, tumpuan.\n
patiṭṭhita: (pp dari **patiṭṭhahati**) tegak dalam, mantap dalam, tersusun, berdiri, disokong, didirikan, bertumpu pada; nt. pengaturan, penyelesaian.\n
patittha: m.  tepi atau pinggir sungai.\n
patta: 1. nt. sayap burung, bulu sayap; (helai) daun; 2. m. nt. mangkuk, patta (wadah makanan bhikkhu); 3. (pp dari **pāpuṇāti**) a. tercapai, didapatkan, diperoleh, menjadi, sampai pada, dilanda; dengan, setelah, terkuasai; **~ādhāraka**m. nt. kaki patta, penyangga patta; **~ānumodana** turut bergembira terhadap apa yang telah didapatkan (jasa-jasa kebajikan); **~āḷhaka**takaran mainan; **~kalla**a.  sudah siap, sesuai; **~kāla** m. sudah tiba waktunya, sudah saatnya; **~kkhandha**a.  dengan “pundak seperti daun”, dengan pundak terjuntai, lesu, putus asa, kecewa, kesal, murung.\n
patti: f. 1.  yang berjalan kaki, pasukan infanteri; 2. perolehan, pencapaian, jasa-jasa kebajikan, manfaat, keuntungan; 3. daun, bagian tumbuhan yang berdaun;  **~dāna** pelimpahan jasa.\n
pattha: m.  suatu tempat terpencil; satu Prastha (suatu ukuran kapasitas), ukuran takaran, = ¼ **āḷhaka**; sejenis alat masak yang berisi satu Prastha.\n
pattharati: menebarkan, membentangkan, merentangkan, menyebar (ke), memancar.\n
pattheti: (**patthayati**) menginginkan, mendambakan, mendoakan.\n
patha: m.  jalan, cara, modus, saluran.\n
pada: nt.  kata (_padaso_), frasa, kalimat, larik; peraturan (_sikkhāpada_), ayat, doktrin agama, ajaran, wejangan, tempat atau keadaan; kaki, telacak, jejak kaki (_gopada_), jalan, posisi (_nakkhattapada_); Nibbana; **~ṭṭhāna** nt. pijakan, tumpuan; sebab terdekat (langsung).\n
padakkhiṇā: f.  hal mengarah sisi kanan, berjaln melingkari (sesuatu atau seseorang) dengan senantiasa mengarahkan sisi kanan badan padanya (untuk menunjukkan sikap penghormatan); pradaksina; “yang mengedepankan kanan”, terampil, pandai, cerdas (dalam belajar); beruntung, penuh berkah, berhasil guna baik. [pradaksina ← Skt. pradakṣiṇa]
padahati: berjuang, berupaya, berusaha, menantang, berdiri berhadapan.\n
padāḷeti: membelah,  memecah, menusuk, menghancurkan, mencocok, menyobek, menikam, menetas.\n
paduma: nt.  teratai, bunga teratai (_Nelumbium_ _speciosum_). [padma ← Skt. padma]
padesa: m.  tanda atau petunjuk, lokasi, jangkauan, wilayah, daerah, tempat.  [pradesa ← Skt. pradeṡa]
padhāna: a.  yang terkemuka; nt.  daya-upaya.\n
pana: dan, namun, dan kini, lantas, selanjutnya, sementara itu, lagi pula, sedangkan, kalau begitu; jadi; **evañ ca pana** demikianlah maka; **ko pana vādo** apalagi (kalau), tak usah dibilang (kalau); **paneva** bisa jadi, bila, akan hal; **vā pana** atau lainnya.\n
panasa: m.  nangka (PED &amp; KLIT: _Artocarpus integrifolia_; KBBI: _Artocarpus heterophyllus_).\n
paneti: membawa menuju, mengenakan, menerapkan.\n
papa: nt. air; balai air, rumah penderma air.\n
papañca: 1. rintangan, hambatan, beban penunda, penunda; 2. ilusi, obsesi, rintangan kemajuan spiritual; 3. hal penyebarluasan, pelipatgandaan, penguluran.\n
papatati: jatuh tersungkur, jatuh, terjatuh dari, roboh, terjatuh kedalam, terjun; aor. **papatā**.\n
papāta: m.  jatuh; jurang, ngarai, tebing yang curam;  a. jatuh menukik, berujung curam, berakhir mendadak.\n
pappaṭaka: m.  pecahan kecil; serpih; sejenis tanaman air.\n
pabbajati: pergi meninggalkan (kehidupan berumah tangga/keduniawian), pergi bertapa, meninggalkan rumah dan hidup mengembara sebagai seorang petapa.\n
pabbajita: (pp dari **pabbajati**) yang telah pergi meninggalkan kehidupan berumah tangga.\n
pabbajjā: f.  meninggalkan keduniawian, menjalankan kehidupan petapa, hal menjadi seorang rahib Buddha (bhikkhu).\n
pabbata: m.  gunung, pegunungan, bukit, batu (karang); **~khaṇḍa** m. nt. jalan pintas sempit di daerah pegunungan; celah patahan pegunungan.\n
pabbateyya: a.  berhubungan dengan gunung, berasal dari gunung, berhulukan gunung.\n
pabbājeti: (kaus. dari **pabbajati**)  membuat pergi meninggalkan, mengusir; membuat seseorang hidup sebagai seorang petapa atau bhikkhu, membuat seseorang meninggalkan kehidupan berumah tangga; menahbiskan.\n
pabbhāra: m.  lereng, landaian, condong.\n
pabhagga: (pp dari **pabhañjati**)  dihancurkan, dimusnahkan, ditaklukkan, dikalahkan.\n
pabhāsati: 1. bersinar; 2. memberitahu, menceritakan, menyatakan, bercerita.\n
pabhāseti:  (kaus. dari **pabhāsati**)  menyinari, menerangi, mencerahi.\n
pamatta: (pp dari **pamajjati**) lengah, lalai, tidak peduli.\n
pamāṇa: nt.  ukuran, jumlah, banyaknya, bilangan, permana, lama, besar, panjang, batas, baku, definisi, dimensi, sifat. [permana ← Skt. pramāṇa]
pamāṇika: a.  membentuk atau mengambil suatu ukuran atau standar, berukuran; orang yang mengukur, hakim, penilai; sesuai (batas) ukuran; memiliki batas ukuran.\n
pamāda: m.  kelengahan, kealpaan, kelalaian, kesembronoan, kelambanan, kekelesaan, ketidakcekatan.\n
pamukha: a.  di depan muka, bagian depan, pertama, terdepan, kepala atau ketua, pamong, terkemuka; **pamukhe** sebelum; **buddha~** dikepalai Buddha. [pramuka ← Skt. pramukha]
pamuñcati: melonggarkan, melepaskan, melontarkan, memancarkan; menaggalkan, meninggalkan, membebaskan.\n
pamutta: (pp dari **pamuñcati**)  dilonggarkan, dilepaskan, dilontarkan; dibebaskan, terlepas.\n
payutta: (pp dari **payuñjati**) tercantol pada; diterapkan, diupayakan, dikerahkan, diabdikan pada, sibuk dalam, terlibat dalam; dapat diterapkan; dapat dijalankan; terencana, disusun, dilakukan, ikhtiar.\n
payoga: m.  cara, sarana, alat; persiapan, usaha, pekerjaan, kesibukan, pelaksanaan, urusan, tindakan, praktik, kesempatan, kejadian;  **ekena payogena**sekaligus.\n
payojana: nt.  memikul (mengurus), urusan; perjanjian; ketetapan, ketentuan; tujuan; hal menerapkan, memakai atau menggunakan.\n
payojāna: nt.  hal menerapkan, memakai atau menggunakan.\n
para: a.  lain, yang lain (_ko paro_ siapa lagi, siapa yang lainnya), asing, di pihak/sisi lain dari, yang di seberang (_paragaṅgāya_); di atas (sana), nun jauh di sana (_paraloko_ dunia mendatang); **paro … paro** satunya ….. lainnya …..; **paro paraṁ**satu sama lainnya; **pare** (pl.)  pihak yang di seberang sana, penganut paham non-Buddhis; **parena** setelah itu; **pare** (lok.) sebelumnya, di masa mendatang, hari sebelum kemarin, hari setelah besok; **paraṁ**adv. menjauh (dari), setelah, lebih lanjut, di pihak atau sisi lain dari, lebih dari itu (_titthiyā hi cattāḷīsaṁ yeva kappe saranti na tato paraṁ_);_  paraṁ maraṇā_ setelah meninggal; _ito paraṁ_ dari sini, setelah ini, selanjutnya, lantas.\n
parakkama: m. upaya, usaha, perjuangan, kegigihan.\n
parakkamati: maju, berupaya, berikhtiar, berusaha, menganju(r), melakukan.\n
paradārika: m.  penggoda istri orang lain, pezina.\n
parama: a.  yang ter…, yang tertinggi, yang terbaik, superior; **~ttha**yang paling hakiki.\n
paramparā: f.  “setelah yang lainnya”, rangkaian, berturut-turut, beruntun, bersambung.\n
paravāda: m. perkataan atau ujaran atau ajaran (pihak) lain, desas-desus masyarakat; pandangan (pihak) lain (sesat).\n
parasuve: adv.  lusa.\n
parahiyyo (parahīyo): adv.  kemarin dulu.\n
parājeti: mengalahkan, menaklukkan, mencundangi; mengecundangi atau mempecundangi (menjadikan kalah);  pass. **parājīyati** atau **parajjhati**.\n
parāmasati: menyentuh, menggenggam, berhubungan, mengambil, melekat, menjadi korban, meraba-raba, memegang-megang, menggerayangi.\n
parāmasana: nt.  hal menyentuh, menggenggam, memegang, mengambil, meraba.\n
parāmāsa: m.  penyentuhan, penggenggaman, kemelekatan, di bawah pengaruh.\n
parāyana (parāyaṇa): nt. tujuan akhir; sokongan, kedamaian; penembusan, pengakhiran, sasaran, melekat pada, menargetkan, mencari dukungan dalam; mengarah pada, akan terlahir di.\n
parikaddhaṇa: nt. menarik, menyeret, menghela.\n
parikanta: a.  membelah, menyobek.\n
parikappa: m.  persiapan, niat, perencanaan, persekongkolan, strategi, siasat; asumsi, pengiraan, praanggapan, dugaan, sangkaan.\n
parikamma: nt.  “mengerjakan sana-sini”, hal membereskan, menyiapkan, mengatur, membenahi, menata, menyusun, mengadakan pelayanan (terutama menggosok dengan minyak), persiapan, awal; _parikammaṁ karoti_ mempersiapkan, mengadakan; **~°** dengan.\n
parikkamana: nt.  berjalan mengelilingi.\n
parikkhaya: m.  aus, susut, lapuk, hilang, berakhir.\n
parikkhāra: m.  “yang mencakup semua”, dandanan, barang perlengkapan, keperluan, barang tambahan, aksesori, peralatan, perkakas; perlengkapan atau keperluan yang meliputi _cīvara_ (jubah), _piṇḍapāta_ (makanan derma), _senāsana_ (kediaman atau peristirahatan), dan _gilāna-paccaya-bhesajja_ (obat-obatan); kadang-kadang juga merujuk ke delapan perlengkapan bhikkhu (_aṭṭha\\uf02dparikkhāra_) yakni _ticīvara_ (tiga jubah), _patta_ (patta), _vāsi_ (pisau cukur), _sūci_ (jarum jahit), _kāya-bandhana_ (ikat pinggang), dan _parissāvana_ (saringan air).\n
parikkhitta: (pp dari **parikkhipati**)  dikelilingi, ditebarkan, dilapisi, dilingkupi, dipagari, dililiti, dibalut.\n
parikkhipati: melingkari, membalut, meliliti, mengelilingi.\n
parigaṇhāti: memeluk, menggenggam, mengambil, memegang, menangkap, meraup; menjelajahi; kaus. **pariggaheti**memeluk, memahami, memiliki, menguasai, menjelajahi, menyelidiki, menemukan; terdiri dari; merangkum.\n
pariggahita: (pp dari **parigaṇhāti**)  diambil, digenggam, dipegang, didatangi, diduduki, dikuasai, dirasuki, dimiliki, dipunyai.\n
paricaya: m.  pengakraban, pengenalan, latihan; akrab dengan, mahir dalam.\n
paricarati: bergerak ke sana-sini, berjalan ke sana-sini, mondar-mandir, berkeluyuran, pindah, mengusahakan, mengurus, memelihara, merawat, melayani; menyembah; mengembara, menjelajahi, menyenangkan (memuaskan) indria sendiri, menghibur diri, bersenang-senang, bermain-main, berolahraga.\n
paricāreti: (kaus. dari **paricarati**)  melayani, merawat, menghormati, menyembah; menghibur diri, bersenang-senang, mendapat kenikmatan.\n
paricita: a.  1. dikumpulkan, ditambahkan; 2. diketahui, dicermati, terbiasa, terampil, dikenal, akrab dengan, senantiasa diamalkan.\n
paricca: ‘berjalan mengelilingi’, melingkupi, menangkap, memahami, menemukan, mengerti.\n
pariccajati: melepaskan, menanggalkan, merelakan, meninggalkan, mengikhlaskan.\n
pariccatta: (pp dari **pariccajati**)  dilepaskan, ditinggalkan, dibuang.\n
pariccāga: m.  hal merelakan, mengikhlaskan, melepaskan, menanggalkan, mengorbankan (misalnya istri, anak, kerajaan, jiwa, dan anggota badan); biaya (pengeluaran); pemberian atau derma (untuk orang miskin), kemurahan hati.\n
parijana: m.  “orang di sekeliling”, pelayaan, pengikut, pembantu, iring-iring, abdi.\n
parijānāti: betul-betul mengetahui˴ memahami˴ mengerti.\n
pariññā: 1. f.  pengetahuan yang akurat atau tepat benar, pemahaman, pengertian utuh; 2. memiliki pengetahuan atau pengertian penuh (ger. dari **parijānāti**).\n
pariññāta: (pp dari **parijānāti**) yang telah betul-betul diketahui˴ dipahami˴ dimengerti.\n
pariññeyya : (grd dari **parijānāti**)  a.  yang seyogianya betul-betul diketahui˴ dipahami˴ dimengerti.\n
pariṇāma: m.  perubahan, transformasi, pencernaan; matang; perjalanan, perkembangan (pengembangan), pemenuhan, nasib, takdir.\n
pariṇāmana: nt.  diubah atau dibelokkan (ke diri sendiri).\n
pariṇāyaka: m.  pemimpin, pembimbing, penutur, penasihat.\n
parittaka: m. kecil, sedikit, secuil, sepele, remeh.\n
parittāṇa: nt. perlindungan, pengamanan, naungan, penangkal.\n
paridaṇḍa: a.  “dikitari tongkat pemukul”, terhukum, sedang dihukum, dilindungi denda.\n
paridahati: mengenakan/memakai (pakaian).\n
parideva: m.  ratap-tangis.\n
pariniṭṭhita: a.  sudah diselesaikan, dibereskan, dikerjakan, dituntaskan.\n
paripakka: a. (cukup) matang, masak, berkembang; terlalu matang, membusuk.\n
paripatati: jatuh.\n
paripantha: m. seputaran, pinggiran, perbatasan, sempadan; rintangan, halangan, hadangan, hambatan, ancaman bahaya.\n
paripāka: m.  matang, masak, berkembang, sempurna; lapuk.\n
paripuñchati: menyeka, membersihkan, menjatuhkan.\n
paripuṇṇa: (pp dari paripūrati)  a. (cukup) penuh, lengkap, utuh, selesai. [paripurna ← Skt. paripūrṇa]
paripūrati: menjadi penuh, lengkap, sempurna; kaus. paripūreti memenuhi, menambahkan.\n
paribbaya: m.  pendapatan, gaji, upah, biaya, pengeluaran.\n
paribbāja(ka): m.  pengelana, pengembara; petapa pengembara yang menganut berbagai pendapat terhadap dunia ini dan suka berdebat (ada enam yang sangat terkenal pada zaman Sang Buddha).\n
paribhāvita: (pp dari **paribhāveti**)  terserap, tersusup, dirawat, disuplai, diisi dengan, terlatih, teratur, dicampur dengan, diperkuat, dierami.\n
paribhāveti: merembesi, menyusup, merawat, menyuplai (membekali).\n
paribhāsa: m.  celaan, kecaman, _makian_, cacian. [peribahasa ← Skt. paribhāṣā]
paribhāsati: memaki, menghardik, mencemarkan nama baik.\n
paribhinna: (pp dari **paribhindati**)  terpecah, tercerai-berai, dipecah-belah, dibelah, dijelek-jelekkan.\n
paribhuñjati: menikmati, menggunakan, menikmati penggunaan dari, menghayati; memurnikan, membersihkan.\n
paribhoga: m.  penggunaan (_theyyaparibhoga_), penikmatan; makanan; barang gunaan/nikmatan, barang milik (_paribhogacetiya_). [periboga ← Skt. paribhoga]
paribhojaniya: nt.  air pencuci, air pembasuh (pembilas).\n
parimajjati: mengusap, menyentuh, menyeka, menggosok.\n
parimaṇḍala: a.  bulat, bundar, melingkar, mengesankan; lengkap, benar, menyenangkan.\n
parimukha: a.  berhadapan, di depan, di muka; nt. adv. **parimukhaṁ** di depan, di muka.\n
pariyatti: f.  kelayakan, kecukupan, kepantasan, hal memadai, kemampuan, kesanggupan, kecakapan, kepandaian; kecakapan dalam Kitab Suci, hal mempelajari (menghapal) Kitab Suci; Kitab Suci; **~dhamma**m.  yang tercakup dalam mempelajari Kitab Suci.\n
pariyanta: m.  akhir, batas, pinggiran, puncak (maksimal).\n
pariyāgāra: a.  dikelilingi sepenuhnya dalam rumah, dilingkupi paviliun.\n
pariyādāna: nt.  habis, terambil semua, tercakup.\n
pariyādāya:  (ger. dari **pariyādati**) (amat) mencengkam (=**sabbato**), memikat, memesona.\n
pariyāpajjati: diselesaikan.\n
pariyāpanna: (pp dari **pariyāpajjati**)  “telah sepenuhnya masuk ke dalam”, tercakup dalam, termasuk dalam, masuk ke dalam (**patta~** yang telah dimasukkan ke dalam patta, yang berada di dalam patta); ulung, pandai, menguasai.\n
pariyāpuṇāti: mempelajari, menguasai, menyelami, mengetahui (melakukan sesuatu), mampu untuk.\n
pariyāya: m.  putaran/giliran (_Kassa nu kho ānanda ajja pariyāyo bhikkhuṇiyo ovadituṁ_), jalan, jalur; cara (_iminā pariyāyena veditabbaṁ _ itu seyogianya dipahami secara demikian), aspek; kebiasaan (_cetopariyāya_); diskusi, wejangan (_madhupiṇḍika-pariyāyo tveva naṁ dhārehi_), metoda, alasan, sebab, dalih, dasar, sinonim, kualitas. [Menurut Buddhaghosa, _pariyāya_ mengandung tiga arti : _desanā_ (ajaran, wejangan), _vāra_ (giliran atau putaran) dan _kāraṇa_ (sebab, alasan, cara, metoda).]
pariyāyena: menurut cara pengajaran dalam Suttanta; dengan menggunakan bahasa perlambang, kiasan atau analogi.\n
pariyāhanana: nt.  pembenturan, penghantaman.\n
pariyesati: mencari, melihat, menyelusur, mendambakan, mengharapkan.\n
pariyodāta: a.  sangat bersih, murni; sangat pandai, terampil, unggul, ulung.\n
pariyonaddha: (pp dari **pariyonandhati**)  a.  yang tertutup, terselubungi, terbungkus.\n
pariyonandhati: mengunci, menempatkan di atas, menutupi, menyelubungi.\n
pariyosāna: nt. bagian akhir; kesempurnaan.\n
pariyosāpeti: memenuhi, menyelesaikan, membereskan, menuntaskan.\n
pariḷāha: m.  pembakaran, kobaran api, demam, demam nafsu, sakit paru-paru; kesukaran, kesakitan.\n
parivaṭṭa: nt.  putaran, ronde.\n
parivattaka: m.  putaran.\n
parivattati: membalik, memutar, pindah; mengubah.\n
parivasati: berdiam, tinggal, berada dalam (menjalani) masa percobaan.\n
parivāra: m.  kerubutan, pengiring, pendamping, pengikut, rombongan, pariwara; pengagung, pengiring atau milik lambang keagungan, gengsi, martabat; bahan-bahan, ramuan, aksesori, pelengkap, perlengkapan; nama kitab terakhir dari _Vinaya Piṭaka_. [pariwara ← Skt. parivāra]
parivāsa: m.  persinggahan, hal berdiam atau tinggal; masa percobaan.\n
parivitakka: m. refleksi, meditasi, pikiran, pertimbangan, perenungan (_cetaso_ _parivitakka_ perenungan batiniah).\n
parivisati: melayani (dengan makanan), meladeni, menghidang, menyajikan, menjamu.\n
parivuṭṭha (parivuttha): (pp dari **parivasati**)  telah berdiam atau tinggal (sekian lama), telah hidup di bawah (menjalani) masa percobaan.\n
parivuta: (pp dari pari + vṛ) dikelilingi, dikerumuni, dikerubuti, dikemas.\n
pariveṇa: nt.  yang menjadi bagian dari suatu benteng, istana dan bagian-bagiannya; sel, bilik kecil, ruangan, lingkungan.\n
parisaṅkā: f.  kecurigaan, khawatir, was-was.\n
parisaṅkita: (pp dari **parisaṅkati**)  dicurigai, mencurigai, khawatir, takut.\n
parisā: f.  kerumunan orang, orang-orang di seputar, kelompok, masyarakat, kalangan, grup, komplotan, kumpulan, himpunan, peguyuban, perkumpulan, perserikatan, orang banyak, persekutuan, pertemuan, majelis. [parisada ← Skt. pariṣad)
parisuddha: a.  bersih, jernih, murni, sempurna.\n
parisedita: (pp dari **parisedeti**) dipanasi, dierami, dimatangkan, dihangati.\n
parisedeti: mengerami, memanaskan dengan uap, mematangkan, duduk mendekam, duduk menderam.\n
parisodheti: membersihkan, memurnikan.\n
parissāvana: nt.  penyaring air, saringan, filter.\n
parihaṭa (parihata)  : (pp dari **pariharati**) dikelilingi oleh, dilingkupi; **sukha~** diliputi keberuntungan, diliputi kebahagiaan.\n
pariharati: menjaga, merawat, melindungi, mengayomi, menaungi, memelihara; membawa serta, membawa berkeliling, mengelilingi, beredar, menyembunyikan, menggelapkan, mengelak dari.\n
parihaseti: menertawai, mengolok-olok.\n
parihāra: m.  perhatian, penjagaan, perlindungan, pengasuhan; kehormatan, hak istimewa, martabat; (tanah) seputar atau sekeliling; pengepungan, penyerangan; penghindaran, pengelakan; **~patha** m. permainan galasin, “_hopscotch_“. [pelihara ← Skt. parihāra]
palāyati: melarikan diri, lari pergi.\n
palāla: m. nt.  jerami.\n
palita: a. abu-abu, kelabu.\n
palobheti: menginginkan, mendambakan, serakah terhadap.\n
pallaṅka: m.  bersila; dipan; _pallaṅkaṁ ābhujati_  (duduk) bersila.\n
pallatthikā: f.  (duduk) bertinggung (duduk dengan lutut terangkat ke atas seperti berjongkok; duduk melipat kaki seperti anjing duduk); berambin (lutut) [duduk dengan tangan disengkelitkan di muka lutut].\n
pallala: nt.  rawa, paya; kolam atau telaga kecil.\n
pavattati: bergerak maju, bergelinding, mengalir, memutar; ada, eksis, berlangsung, menghasilkan.\n
pavattana: a. nt.  hal bergerak maju, bergelinding, memutar, melaksanakan, melakukan; bermanfaat; eksis.\n
pavatti: 1. bentuk _aorist_ dari **pavattati**; 2. kejadian, insiden, berita, perwujudan.\n
pavatteti: (kaus. dari **pavattati**) mendorong, menggerakkan, menggelindingkan, memutar; menyebabkan, menghasilkan, membangkitkan; memberikan; melanjutkan, mempraktikkan; mondar-mandir, mempertunjukkan, melaksanakan, menjalankan, menyelenggarakan, mengamalkan.\n
pavara: a.  terunggul, mulia, terkemuka.\n
pavāta: nt.  aliran udara, hembusan angin, badai, gelora.\n
pavijjhati: melempari, melontarkan.\n
paviṭṭha: (pp dari **pavisati**)  dimasuki, masuk, dikunjungi.\n
pavisati: pergi ke, memasuki.\n
pavuttha:  (pp dari **pavasati**)  berdiam atau tinggal di luar (atau jauh dari) rumah; **~jāti**orang yang tidak termasuk dalam kasta apa pun; **~patikā itthi** seorang wanita yang suaminya tidak berdiam di rumah (sedang merantau atau bepergian).\n
paveṇi: f.  kepang rambut; tikar, penutup; adat, tradisi, kebiasaan; silsilah, keturunan, ras.\n
pavedeti: memaklumkan, menyatakan, mengungkapkan, menyampaikan.\n
pavesana: nt.  hal masuk, mulai, awal pemasukan; penerapan; cara masuk;  a.  mampu masuk.\n
paveseti: (kaus. dari **pavisati**) membuat masuk, membolehkan masuk, mengantar; menyediakan, memasok, memperkenalkan, memperoleh, menerapkan pada.\n
pasaṁsati: berterus terang, menyanjung, memuji, mengakui, berkenan.\n
pasattha (pasaṭṭha): (pp dari **pasaṁsati**)  dipuji, disanjung, diagungkan.\n
pasanna: 1. (pp dari **pasīdati**) jernih, bersih, terang, cerah; bahagia, gembira, senang; tenteram, damai, puas, percaya, yakin, saleh, baik, bajik; 2. mengalir keluar, mengucur.\n
pasambheti: (kaus. dari **passambhati**) menenangkan; ppr. **passambhayaṁ**.\n
pasayha: (ger. dari **pasahati**)  menggunakan kekerasan, dengan kekuatan.\n
pasavati: mendatangkan, melahirkan, menimbulkan, menghasilkan,  menimbun.\n
pasahati: menggunakan kekuatan atau kekerasan, menekan, menaklukkan, menundukkan, mengatasi.\n
pasāda: m.  kejernihan, kecemerlangan; kegembiraan, kepuasan, kebahagiaan, kedamaian batin, keyakinan, tulus-yakin, ketenteraman, ketenangan, transparan; ~bhañña ungkapan keyakinan.\n
pasādhana: nt.  hiasan, dekorasi, ornamen, dandanan.\n
pasādheti: menghiasi, memperindah, mendandani.\n
pasārita: (pp dari **pasāreti**)  merentangkan, membentangkan, memaparkan, menggelar, menawarkan.\n
pasāreti: mendorong, melepaskan; merentangkan, membentangkan, menggelar, menawarkan.\n
pasibbaka:   m. nt.  kantung.\n
pasīdati: menjadi terang/bening, mencemerlangkan, dimurnikan, akur, berkenan; jelas dan tenang, menjadi tenteram, meyakini.\n
pasuka (pasu): m.  ternak, lembu, sapi.\n
pasuta: a.  melekat pada, berniat akan, melakukan, mengikuti.\n
passa: 1. melihat, orang yang melihat; 2. m. nt. sisi, samping, sayap, lereng.\n
passati: melihat, menyaksikan, menemukan, mengetahui, menyadari, memahami, mencari.\n
passaddha: (pp dari passambhati) a.  tenang, diam, kalem, damai, hening.\n
passaddhi: f.  ketenangan, kedamaian batin, keheningan.\n
passambhati: menenangkan, diam, tenang, damai.\n
passasati: menghembuskan napas.\n
passāva: m.  air kencing, air seni, kemih; **~magga**lubang kemaluan.\n
pahaṭṭha: (pp dari pahaṁsati) 1. dipukul, dihantam, ditempa; 2. gembira, bahagia, bersuka cita.\n
paharati: memukul, menghantam, menggebuk, mendera, menyerang; kaus. **paharāpeti** menyuruh atau membuat diserang, mengenakan, menghubungkan, mengaitkan.\n
pahāna:   nt. hal meninggalkan, menanggalkan, melepaskan, mengenyahkan, menyingkirkan, menghindari, menolak.\n
pahāra: m.  1. pukulan, hantaman, tonjokan, gebukan, deraan, benturan; 2. waktu jaga (= **yāma**).\n
pahiṇati: mengirim, mengutus.\n
pahita: (pp dari **padahati**) dikirim; gigih, bersemangat, bertekad bulat.\n
pahitatta: m. kegigihan, tekad bulat.\n
pahīyati: (pass. dari **pajahati**) ditinggalkan, ditanggalkan, dienyahkan, disingkirkan, lenyap, hilang, memudarkan.\n
pahīna: pp dari pajahati) telah ditinggalkan, ditanggalkan, dienyahkan, dihancurkan, disingkirkan.\n
pahūta: a.  cukup, banyak, berlimpah, lumayan.\n
pahoti: mengeluarkan, menimbulkan, memunculkan; [bersama inf.] cukup, sesuai, mampu.\n
pākata (pākaṭa): a. umum, biasa; tak terkendali, liar, vulgar, bersimaharajalela, terbuka, nyata, tersingkap, diketahui umum, dikenal luas; _pākataṁ karoti_ menyingkapkan.\n
pākāra: m.  tembok pengeliling, didirikan sebagai penghalang dan pelindung, pagar, kubu, benteng.\n
pācittiya: sejenis pelanggaran winaya yang harus ditebus atau diakui di depan seorang bhikkhu. Pelanggaran ini termasuk pelanggaran ringan (_lahukāpatti_).\n
pācīna: a.  timur.\n
pājeti: mengendarai, berkendaraan, berwahana; melempar (dadu).\n
pāṭikulyā (pāṭikulyatā): f.  hal memuakkan, hal menjijikkan, hal tidak menyenangkan, hal menyebalkan.\n
pāṭipuggalika: a.  bersifat individu.\n
pāṭimokkha (pātimokkha): nt.  kumpulan peraturan yang harus dipatuhi para bhikkhu, perangkat asas dasar pengamalan ajaran.\n
pāṭihāriya: a.  mencengangkan, menakjubkan, luar biasa, istimewa; nt. keajaiban, kekuatan gaib, mukjizat.\n
pāṭha: m.  bacaan, teks, wacana, kalimat, lektur, ayat.\n
pāṇa: m.  napas, kehidupan, makhluk hidup.\n
pāṇaka: a.  yang hidup, makhluk hidup; ulat, serangga, kutu.\n
pāṇi: m.  tangan.\n
pāṇin: a.  bernyawa, makhluk hidup.\n
pāta: m.  jatuh; lempar, lemparan.\n
pātavyatā: f.  keruntuhan, kejatuhan, penjatuhan, perontokan, hal terperosot ke dalam.\n
pātāpeti: menjatuhkan, menyuruh melakukan abortus.\n
pātī (pāti): f. mangkuk, wadah, patta.\n
pātubhāva: m.  kemunculan, pemunculan, perwujudan.\n
pātur: tampak, terungkap, muncul; pātukaroti memunculkan;  pātubhavati muncul.\n
pāteti: menjatuhkan, melemparkan; membunuh, menghancurkan, memancung (memenggal).\n
pāto: di pagi hari.\n
pāda: m. nt.  kaki, langkah, telapak kaki, landasan atau dasar; seperempat dari sesuatu (dari syair misalnya, baris); mata uang (logam) ( = 5 māsaka).\n
pāna: m.  minuman; **~āgāra** nt. kedai minuman.\n
pānīya (pāniya): a. nt.  yang dapat diminum; minuman, air minum.\n
pāpa: a.  jahat, buruk, nista, berdosa, brengsek; tak subur; nt. kejahatan, kesalahan, dosa. [papa ← Skt. pāpa]
pāpaka: a. buruk, jahat, nista, berdosa, brengsek, rendah.\n
pāpuṇāti: mencapai, meraih, memperoleh, tiba pada, menguasai, menggenapi, mencukupi.\n
pāpeti: 1. memburukkan, menjelek-jelekkan, membuat malu; 2. (kaus. dari **pāpuṇāti**) membuat mencapai, membawa menuju.\n
pāmaṅga: nt.  pita, pembalut, rantai.\n
pāmojja (pāmujja): nt.  suka-cita, kegembiraan, senang, girang.\n
pāyeti: (kaus. dari **pibati**)  membuat terminum, memberi minum, meminumkan, mengairi.\n
pārisuddhi: f.  hal murni, kemurnia, pemurnian, kesucian, penyucian.\n
pāra: a.  di sana, seberang sana, lewat; nt. seberang sana; **pārato** dari sisi lain.\n
pāramī: f.  kesempurnaan; dalam J. 1:73 dan DhA. 1:84 disebutkan ada sepuluh yakni _dāna_, _sīla_, _nekkhamma_, _paññā_, _viriya_, _khanti_, _sacca_, _adhiṭṭhāna_, _mettā_, dan _upekkhā_.\n
pārājika: m.  orang yang telah melakukan pelanggaran sangat serius terhadap peraturan bagi para bhikkhu; dia yang telah takluk.\n
pāricariyā: f.  pelayanan, peladenan, penghormatan.\n
pāripūrī: f. pemenuhan, penyelesaian, penyempurnaan, perwujudan, pelaksanaan, hal melengkapi.\n
pāruta: (pp dari **pārupati**)  tertutup, berpakaian.\n
pārupati: menutupi, mengenakan pakaian, menyelubungi, menudungi, mengerudungi.\n
pālaka: m.  penjaga, penggembala.\n
pāḷi (pāli): f.  garis, deret; teks, babon (naskah asli, naskah sumber) yang bukan _Aṭṭhakathā _; bahasa Pali, bahasa yang berhubungan erat dengan bahasa _Māgadhī _; **~bhāsā** bahasa babon.\n
pāvacana: nt.  kata, sabda (Buddha); zaman pembabaran Dhamma.\n
pāvadati (pavadati): menyatakan, memberi tahu, memperlihatkan, menyampaikan.\n
pāvāra: m.  mantel, jubah; pohon mangga.\n
pāvuraṇa: nt.  mantel, jubah (penghubung).\n
pāsa: m.  jerat, pengikat, belenggu; tombak, lembing.\n
pāsaka: m.  ikatan simpul; lemparan; batu dadu.\n
pāsāṇa: m.  batu.\n
pāsāda: m.  panggung tinggi, podium tinggi; bangunan yang berdiri di atas fondasi yang tinggi, teras; pancapersada, persada; istana; bangunan yang besar dan panjang, bangunan bertingkat; tanah atau landasan yang lebih tinggi daripada tanah sekelilingnya. [persada ← Skt. prāsāda]
pāsādika: a.  menyenangkan, bagus, seronok (menyenangkan hati; sedap dilihat, didengar dsb), ramah, nyaman, kebeningan, kejernihan.\n
pāsuḷa: m.  rusuk.\n
pāhuṇa: m.  tamu, suguhan untuk tamu, hadiah.\n
pāhuṇeyya: a.  layak/patut menerima suguhan.\n
pāheti: mengirim, mengutus.\n
pi: ☞  api
piṭaka: m.  keranjang; kumpulan kitab suci.\n
piṭṭhi (piṭṭhī): f.  1. punggung, bagian atas, susur; **piṭṭhito** adv. dari (di) belakang; _piṭṭhito anubandhati  _mengikuti (menguntit) dari belakang; _piṭṭhito karoti_  meninggalkan, membelakangi; **piṭṭhito piṭṭhito** sangat dekat di belakang, ketat, rapat.\n
piṭṭhika: a.  berpunggung.\n
piṇḍa: m.  gumpalan, bulatan; gumpalan makanan, makanan derma dalam bentuk bulatan; **~cārika** m.  orang yang pergi berpindapata; **~pāta** m. makanan derma (yang diterima dalam patta), pindapata; hal berpindapata; **~pātika** m. orang yang hanya menyantap makanan yang diterima dalam pattanya (yang hanya makan dari hasil pindapata).\n
piṇḍaka: m.  makanan (derma); _na piṇḍakena kilamati_  tidak kekurangan makanan; _ukka-piṇḍaka_  segerombolan serangga atau kutu.\n
pitar: m.  ayah.\n
pitāmahā: m.  kakek.\n
pitta: nt.  empedu; empedu juga berfungsi sebagai tempat asal kemarahan atau kegembiraan; **baddha~** organ empedu; **abaddha~** cairan empedu; bengkakan, kerumunan; kandung kemih.\n
pithīyati (pithiyyati): (pass. dari **pidahati**)  ditutupi, dihalangi, dirintangi, menutup.\n
pidahati: menutup.\n
pipāsā: f.  kehausan, kelaparan, keinginan, dambaan, hasrat, haus-damba.\n
piya: a.  yang dikasih, disayang; menyenangkan, disukai, berkenan di hati, kinasih (sangat dikasihi).\n
pilandhana (piḷandhana): nt.  menghiasi, berhiaskan, perhiasan.\n
pilotikā: f.  sepotong kain kecil, secarik kain, pembalut (perban).\n
pivati: (**pibati**) minum, menenggak, meneguk.\n
pisati: (**piṁsati**) menggiling, melumatkan, meremukkan, menghancurkan.\n
pisuṇa: a.  memfitnah, mengadu domba, bergunjing.\n
pīṭha: nt.  bangku, kursi bersandaran tegak, dipan (lebih pendek dari ranjang, tetapi tidak sampai berbentuk persegi).\n
pīṭhaka: m.  kursi, bangku (tak bersandaran), dipan.\n
pīta: 1. (pp dari **pivati**) telah diminum, dibasahi, diresapi, dirembesi; 2. a. kuning, emas, kuning kecoklatan.\n
pītaka: a.  kuning.\n
pīti: f.  kegembiraan, kegiuran (batin) [bukan perasaan tetapi sebagai suatu wujud reaksi batin].\n
pīna: a.  gemuk, gembung.\n
pīḷita: (pp dari **pīḷeti**)  tergilas, tertekan, ditindas, terdesak, dilanda, diimpit, dianiaya, diganggu, diusik.\n
pīḷeti: menekan, menindas, memberati, memencet, mengimpit, menggilas, menundukkan, menganiaya, melanda, mengganggu.\n
puggala: m.  individu, perorangan, orang, pribadi, sifat, jiwa.\n
pucimanda: nama pohon (_Azadirachta indica_); pohon nimba.\n
pucchati: bertanya, mempertanyakan; mengundang, menawarkan, memberikan kepada seseorang, bertanya dengan; pass. **pucchīyati**.\n
pucchā: f.  pertanyaan.\n
puñja: m.  onggokan, tumpukan, pumpunan; **~kita**a. onggokan, tumpukan.\n
puñña: nt.  kebajikan, jasa, jasa kebajikan. [punya/punia ← Skt. puṇya]
puññavant: a.  memiliki jasa-jasa kebajikan.\n
puṇḍarīka: nt.  teratai putih.\n
puṇṇa: a.  penuh. [purna ← Skt. pūrṇa]
putta: m.  putra; anak, keturunan. [putra ← Skt. putra]
puttaka: m.  putra, anak kecil; burung belia.\n
puthu: 1. a.  secara terpisah, masing-masing; adv.  masing-masing; _puthageva_  masing-masing; 2. menghampar, banyak, beraneka, beragam, luas, kebanyakan; **~sīlā** f. lempengan batu.\n
puthujjana: m.  manusia biasa, orang kebanyakan, orang awam (yang belum melihat empat Ariyasacca).\n
puthula: a. lebar, luas, lapang, datar.\n
puna: lagi; **puna** **caparaṁ**  dan juga, kemudian dari itu, lagi pula, selain itu.\n
punabbhava: m.  punarbhawa, kelahiran kembali.\n
puppha: nt.  bunga, kembang, puspa; darah (menstruasi). [puspa ← Skt. puṣpa]
pupphati: mekar, mengembang.\n
pubba: a.  sebelumnya, terdahulu, awal, terlebih dahulu; **pubbaṇha**pagi hari; **~bhāsin** yang menegur pertama, yang pertama berbicara. [purwa/purba ← pūrva]
pubbaṅgama: m.  berjalan di depan, mendahului; dikendalikan atau diarahkan oleh, didahulukan, mengawali.\n
pubbaṇṇa: m. serealia terawal, serealia mentah, padi-padian; terdiri dari tujuh jenis : _sāli_ (padi gogo, padi ladang, padi huma), _vīhi_ (beras merah, beras coklat, beras pirang), _yava_ (barli), _godhūma_ (gandum), _kaṅgu_, _varaka_, dan _kudrūsaka_.\n
pubbarattāpararattaṁ: masa lalu dan masa mendatang, segenap waktu, selalu, senantiasa.\n
pubbenivāsa: m.  kediaman atau keadaan dalam kelahiran lampau.\n
pura: 1. sebelum; 2. nt.  kota, benteng, kediaman, rumah, bagian dari rumah; tubuh.\n
purato: di depan (dg gen.), sebelum; **purato** **purato** setiap kali di depan, di depan setiap (masing-masing), terus-menerus di depan.\n
purā: sebelumnya, di masa sebelumnya, di masa lampau.\n
purāṇa: a.  dahulu kala, masa lampau, tua, renta, bekas, usang; sebelumnya, terdahulu, mantan.\n
purima: a.  sebelumnya, terdahulu, lampau.\n
purisa: m.  orang, laki-laki, manusia; pelayan, jongos.\n
purisaka: m.  orang-orangan; a. bersama seorang lelaki.\n
pure: sebelum, di depan, sebelumnya, terdahulu; **puretaraṁ** adv. pertama, terdepan.\n
purekkhāra: m.  bertujuan untuk, dimaksudkan untuk; hal mempersembahkan, menjunjung.\n
pūga: nt.  onggokan, massa, jumlah banyak;  m. persekutuan, peguyuban, perserikatan; sirih, pinang.\n
pūjanā: f.  penghormatan, sembah; persembahan.\n
pūjā: f. penghormatan, pemuliaan, hal berbakti, perhatian, persembahan.\n
pūjita: (pp dari **pūjeti**)  dihormati, dipuja, dilayani.\n
pūjeti: menghormati, memuja, menyembah, memuliakan.\n
pūti: a. (= **kuṇapa-gandha**) membusuk, tengik, busuk menyengat hidung, bangar, kohong.\n
pūra: a.  penuh, penuh dengan, kancap, peres.\n
pūreti: mengisi, memenuhi; kaus.  **pūrāpeti** menyebabkan (menyuruh) mengisi.\n
pūva: m.  kue (kering).\n
pekkhati: melihat, memandang, menengok, menatap, mengamati, menonton.\n
pekkhin: a.  melihat, memandang.\n
pecca: setelah meninggal.\n
peta: arwah mereka yang telah meninggal, hantu, setan kelaparan (senantiasa diliputi haus dan lapar; mempunyai wajah seperti sebuah puncak gunung, perut seperti gunung atau lautan, mulut seperti mata jarum, telanjang, hanya ditutupi rambut. Tampak seperti sebuah nyala api. Mengerang memohon belas kasihan manusia.); f.  **petī**.\n
pettika: a.  pihak ayah.\n
pema: nt.  cinta, kasih, sayang.\n
pemanīya: a.  mengharukan, penuh kasih sayang, ramah, tercinta, menyenangkan.\n
peyya: 1. (grd dari **pibati**) diminum, diteguk, dapat diminum; 2. =**piya** ramah, menyenangkan, berkenan di hati; **~vajja** nt. ucapan yang ramah menyenangkan, ucapan yang berkenan di hati.\n
peyyāla: nt.  pengulangan, silih semilih, rangkaian, rumusan, frasa, cara pengungkapan.\n
pesana: nt.  hal mengirim keluar; pesan; pelayanan; **~kāraka (~kārikā**) pelayan, pembawa pesan. [pesan ← Skt. ?]
pesanika: a.  berhubungan dengan pesan, menyampaikan pesan.\n
pesala: a.  menyenangkan, berperilaku baik.\n
pesi (pesī): f.  gumpalan (daging); potongan, cuil; tahap ke-3 dari perkembangan janin (antara _abbuda_ dan _ghana_).\n
pesita: (pp dari **peseti**) dikirim, diutus, disuruh, diperintahkan, apa yang telah diperintahkan.\n
peseti: mengirim, mengutus; mempekerjakan, menyuruh, memerintahkan;  pass. **pesiyati**diperintahkan, ditugasi.\n
pokkhara: nt.  tanaman teratai, daun teratai; kulit gendang; sejenis unggas air (bangau).\n
pokkharaṇī: f.  kolam teratai, kolam buatan atau telaga kecil untuk tanaman air.\n
poṭheti (potheti): memukul, menepuk; memetik jari.\n
poṇa: a.  melandai turun; cenderung (mudah); condong,  mengarah pada (ke), menuju, tirus, runcing, lancip.\n
potaka: m.  hewan muda, hewan belia, anak hewan;  f. **potikā**;  ranting kecil, cabang, dahan.\n
potthaka: m. nt.  buku, pustaka; kanvas tempat melukis. [pustaka ← Skt. pustaka]
pothujjanika: a.  yang bersifat seperti orang awam, _seperti orang kebanyakan_, umum, biasa.\n
porāṇa: a.  tua, kuno, purba, dahulu; **porāṇā** pl. orang kuno, penulis kuno atau di zaman dahulu.\n
porāṇaka: a. tua, kuno, purba, dahulu; usang, aus.\n
posikā: f.  pemelihara, penyuap.\n
poseti: memelihara, mendukung, mengurus, merawat, mengasuh.\n
phaṇa: m.  tudungan ular; _phaṇaṁ karoti_ menudungi.\n
phandati: berdebar, berkedut, bergetar, guncang, bergerak;  kaus. **phandāpeti**membuat berdebar.\n
pharati: 1. menyebar, merebak (?), memenuhi, menebar, memancarkan, menyiarkan, mengembang, menyusupi, meruyak (?), merasuki (?), meresapi; merangsang; meluas; 2. **atthaṁ pharati** berfungsi sebagai.\n
pharasu: m.  kapak (kayu).\n
pharusa: a.  kasar, keras; kejam, bengis, zalim.\n
phala: nt.  buah; buah pelir, biji kemaluan; hasil, akibat, pahala, ganjaran, (buah) kesucian.\n
phalaka: m.  bilah kayu, papan; perisai; lembaran kayu atau kulit kayu yang digunakan untuk membuat pakaian seorang petapa.\n
phalati: terbelah, terburai; menjadi matang atau masak.\n
phāṇita: nt.  jus tebu, air tebu, sari tebu.\n
phāti: f.  bengkak, mengelembung, mengembang.\n
phāleti: (kaus. dari **phalati**) membelah, memecahkan, memotong, memenggal, mencabik-cabik, menyobek.\n
phāsu: a.  menyenangkan, nyaman; **~vihāra**kenyamanan, ketenteraman.\n
phīta: a.  kaya, makmur.\n
phuṭṭha:  (pp dari **phusati**)  disentuh, dipengaruhi, dilanda, tertimpa, disinggung, disenggol.\n
phusati: menyentuh; mencapai, meraih.\n
phusana: nt.  hal menyentuh.\n
phoṭṭhabba: nt.  sentuhan, kontak.\n
badara: m. nt.  bidara cina (_Zizyphus jujuba_).\n
badarī: f.  bidara cina (_Zizyphus jujuba_).\n
baddha: 1. (pp dari **bandhati**) terikat, dibebat, terbelenggu, terbalut, terjerat, terperangkap; dikukuhkan, dimantapkan, ditambal, mengidap, mendapat, terikat pada, melekat pada, kecanduan terhadap, dipadukan, diberkas, dibendel, diadoni, diuli, dirangkaikan, dihubungkan, dikumpulkan, dihimpun, ditetapkan, dipastikan; 2. nt. selempang kulit, tali kulit.\n
bandhati: mengikat, membebat, membentuk, menyatukan, menambatkan pada, menempatkan di atas (pada), memasang, menyiapkan, memulai, membuat, mendapatkan, menyusun; pass. **bajjhati**.\n
bandhana: nt.  ikat, ikatan, belenggu; tambalan, kumpulan, komposisi, konstitusi; penyatuan, pemaduan, persatuan, (peng)gabungan; pegangan (gagang); sambungan; **~āgāra**nt. rumah tahanan.\n
babbaja: m.  sejenis rumput atau ilalang kasar, biasanya dipakai untuk membuat selipar (sandal).\n
bala: nt.  kekuatan, daya; pasukan, kekuatan militer. [bala ← Skt. bala]
bahi: adv.  luar, bagian luar.\n
bahiddhā: adv.  luar, bagian luar; dengan melangkahi.\n
bahu: a.  banyak, jamak, berlimpah; sangat. [bahu ← Skt. bahu]
bahuka: a. nt.  banyak, berlimpah.\n
bahula: 1. a. banyak, jamak, berulang-ulang, berkali-kali; sangat; nt. banyak, penuh dengan; dengan penuh; 2. nt. nama sejenis undian harapan.\n
bahulikata: a.  diperbanyak, dijamakkan, dilatih, diulang-ulang.\n
bādhati: menekan, memberatkan, menghambat, mendera, merusak; pass. **bādhiyati** didera, menderita; kaus.  **bādheti**; pp. **bādhita**.\n
bādhana: nt.  hal menangkap, melukai, menyakiti, menimbulkan penderitaan; rintangan.\n
bārāṇasī: f. nama ibu kota kerajaan Kāsī (kaum Vajji), sekarang bernama Benares.\n
bāḷha: a.  kuat; **~taraṁ** jauh lebih, amat sangat; **bāḷhaṁ** adv. dengan kuat, sangat, amat, keras.\n
bāla: a. dungu, bodoh, tolol, tak mampu bernalar, tak mampu berpikir dan bertindak dengan baik; muda, belia, baru, segar, awal, dini; kanak-kanak anyir (di bawah 16 tahun); rambut.\n
bālya: nt. masa kanak-kanak, kanak-kanak; kebodohan, ketololan, kegoblokan.\n
bāhā: f.  lengan, tiang (pintu).\n
bāhirima: a.  bagian luar, eksternal.\n
bāhu: m.  lengan. [bahu ← Skt. bāhu]
bāhulla: nt.  kelimpahan, kemewahan; kehidupan yang mewah.\n
bāhullika: a.  hidup dalam kemewahan, mewah, boros.\n
bāhusacca: nt.  hal banyak belajar, hal memiliki pengetahuan mendalam atau banyak.\n
bāheti: menyingkirkan, menyisihkan, menangkal, mengabaikan, mengesampingkan.\n
bimba: nt.  wujud, rupa, gambar; buah merah dari _Momordica monadelpha_ (sejenis bayam).\n
bimbohana:  nt.  bantal (kepala), kalang hulu.\n
bila: 1. nt. lubang, liang, gua, rongga; 2. nt. bagian, cuil; 3. m. sejenis garam.\n
bilaṅga: m.  bubur masam, kanji.\n
billa: m.  buah bilakmata, buah maja (_Aegle marmelos_).\n
bīja: nt.  biji, benih, bibit, (air) mani; unsur. [biji/bijan/wijen ← Skt. bīja/bījin]
bījaka: m.  keturunan.\n
bujjhati: mengalami pencerahan (atas), menyadari, mengetahui, memahami; kaus. **bodheti**, **bujjhāpeti**; pass. **bujjhīyati**.\n
bujjhanaka: a.  memiliki pengetahuan, memiliki unsur pencerahan (bodhi), memiliki batin yang tercerah.\n
buddha: (pp dari **bujjhati**)  paham, sadar, telah mencapai pencerahan; m. orang yang telah mencapai pencerahan.\n
buddhānubuddha: a.  mengalami  pencerahan sempurna; mengalami pencerahan oleh ia yang telah mengalami pencerahan (Buddha).\n
buddhi: f.  kebijaksanaan, kearifan, budi (1. alat batin yang merupakan paduan akal dan perasaan untuk menimbang baik dan buruk; 2. akal atau kecerdikan). [budi ← Skt. buddhi]
budhavāra: m.  Hari Rabu.\n
bodhi: f.  pengetahuan tertinggi, pencerahan (batin); **~pakkhika** (= **pakkhiya**) bagian dari pencerahan (batin); pokok-pokok pencerahan (batin); _penopang (menuju) pencerahan_; **~rukkha** m. pohon Bodhi (_assattha_, _Ficus religiosa_);  **~satta** m. calon Buddha, seseorang yang nantinya akan menjadi Buddha.\n
byañjana: nt.  suku kata; konsonan; tulisan/huruf; ciri/tanda; ungkapan; lauk, masakan kari, makanan penyedap, sambal.\n
byasana (vyasana)  : nt.  musibah, kemalangan, malapetaka, bencana, petaka.\n
byādhi: m.  sakit, penyakit.\n
byāpāda: m.  niat jahat, maksud jahat.\n
byūha: m.  barisan pasukan, tumpukan, kumpulan.\n
brahmacariyā: f.  kehidupan luhur (terutama dalam hal hidup selibat/wadat).\n
brahmacārin: a.  yang menapaki kehidupan luhur, yang mengamalkan kehidupan luhur.\n
brahmattabhāva: m.  keberadaan sebagai Dewa Brahma.\n
brāhmaṇa: m.  orang yang berkasta brahmana; (dalam kitab Buddhisme, acapkali mengandung arti) orang yang hidupnya suci; _brahmana_.\n
brūti: berkata, memberi tahu, menyebut, memperlihatkan, menjelaskan, menguraikan.\n
bhagavant: a. beruntung, mujur, termasyhur, mulia; Yang Mahamulia. [begawan ← Skt. bhagavant]
bhaginī: f.  saudari.\n
bhaṅga: nt.  1. kanvas, mota, terpal, kain rami kasar; 2. pecah, terurai, penguraian, disolusi.\n
bhañjaka: a.  menghancurkan, merusak.\n
bhañjati: memecahkan, meluluhlantakkan, menghancurkan; melipat, menekuk.\n
bhaṭa: m.  pelayan, abdi, orang sewaan, serdadu. [batur ← Skt. bhaṭa]
bhaṇati: berbicara, memberitahu, menyatakan, mendaras.\n
bhaṇe: he coba (gaya bicara orang berkedudukan tinggi kepada bawahannya), begitulah, kiranya, he, coba (lihat), hayo.\n
bhaṇḍa: nt.  stok barang dagangan, barang-barang, milik, harta, banda, benda; peralatan, perlengkapan. [benda/banda ← Skt. bhāṇḍa]
bhaṇḍati: bertengkar, bercekcok, berselisih, berbantah, mencaci-maki.\n
bhaṇḍikā: f.  kumpulan barang-barang, tumpukan, onggokan, bundelan, gepok, gabung, perlengkapan.\n
bhata: a.  dipelihara, dipertahankan, didukung, ditopang, disokong, dilahirkan, menjadi bobot; m. pelayan.\n
bhati: f.  gaji, upah.\n
bhatta: nt.  makanan, nasi; **~sammada** rasa kantuk setelah makan.\n
bhattagga: nt.  ruang makan.\n
bhadanta (bhaddanta): m.  Yang Mulia, Yang Terhormat; vok. sg. **bhadante**; vok. pl. **bhadantā**.\n
bhadda: (**bhadra**) a.  penuh berkah, beruntung, tinggi, luhur, beralamat baik, penuh kebesaran, yang mulia (sebutan untuk orang yang dihormati), baik, bahagia;  nt.  sesuatu yang membawa keberuntungan, keadaan baik, kesejahteraan, kemuliaan, perbuatan baik; sejenis panah; sapi jantan; **~kappa**  m. kappa (kurun waktu) yang penuh berkah, kappa sekarang di mana telah dan akan muncul lima Buddha yakni _Koṇāgamana_, _Kakusandha_, _Kassapa_, _Gotama_, dan _Metteya_.\n
bhaddaka (bhadraka): baik, mulia, terhormat, beruntung, penuh berkah, bernilai.\n
bhamati: berpusing, berputar-putar, mondar-mandir, berkelana.\n
bhamuka (bhamukha) :  f.  alis mata, kening.\n
bhaya: nt.  ketakutan. [bahaya ← Skt. bhaya]
bhayānaka: a.  menakutkan, mengerikan; nt. sesuatu yang menakutkan.\n
bharita: a. dipenuhi dengan, berisikan.\n
bhariyā: f.  “orang yang disokong”, istri.\n
bhava: m.  “mengada, menjadi”, (wujud) kelahiran kembali, (keadaan) keberadaan / eksistensi, “kehidupan”, dumadi.\n
bhavati: menjadi, ada, menjadi ada, berlangsung, terjadi; _hotu_ _bhante_ baik sekali bhante; _na dāni tena ciraṁ jīvitabbaṁ bhavissati_  kini ia takkan hidup lama lagi;_ maggo kho me gantabbo bhavissati_  saya masih harus menempuh jalan.\n
bhavant: tuan, yang mulia, yang terhormat, Anda.\n
bhākuṭika: a.  mengernyitkan alis atau dahi; **~bhākuṭiko** selalu mengernyitkan alis, angkuh; f. **bhākuṭikā** kernyit.\n
bhāga: m.  bagian, porsi, jatah, ranji; **bhāgaso** adv. bagian demi bagian, secara merata, secara proporsional, seturut bagian masing-masing.\n
bhāgineyya: m.  putra saudara perempuan, kemenakan laki-laki.\n
bhāgiya: a.  berhubungan dengan, mendatangkan, menghasilkan, mengakibatkan, memperoleh, mendapat(kan), kelompok dari.\n
bhāgī: a. m.  mengambil bagian, mendapat bagian dari.\n
bhājana: nt.  bejana, wadah penampung; pembagian, penguraian, uraian. [bejana ← Skt. bhājana]
bhājeti: (kaus. **bhajati**)  membagi-bagikan, mengacang, mengagih.\n
bhāṇa:   m.  penuturan atau pelafalan, pelantunan; ~vāra  bab kitab suci, babak tuturan.\n
bhāṇaka: 1. a. menuturkan; penutur, pelantun, pendaras, pengkhotbah; 2. m. kendi.\n
bhātar: m.  saudara.\n
bhāyati: takut; mengancam.\n
bhāra: m.  barang bawaan, beban; muatan; hal yang sulit; beban tugas; ukuran berat emas (1 **bhāra** = 20 **tulā** = 2000 **pala**). [bahara/barang ← Skt. bhāra]
bhāva:   m.  hal mengada, menjadi; kondisi, sifat, keadaan, kehidupan; hal, ihwal; niat, cinta, hasrat, tujuan, kegemaran.\n
bhāvanā: f.  hal menghasilkan, berdiam dalam, mengarahkan pikiran pada, pengamalan, pengembangan batiniah, olah batin.\n
bhāvita: (pp dari **bhāveti**)  dikembangkan, ditumbuhkan, diwujudkan, dibiakkan, terolah, diseimbangkan.\n
bhāveti: menghasilkan, menumbuhkan, melahirkan, memupuk, mengembangkan, membiakkan, bertambah, berkembang.\n
bhāsati: mengatakan, menyatakan, berkata kepada, menyebutkan, membicarakan.\n
bhāsita: (pp dari **bhāsati**)  diucapkan, dikatakan, diutarakan, dikemukakan, dituturkan; nt. ucapan, kata-kata.\n
bhiṁsana: (**bhiṁsanaka**) a.  menakutkan, mengerikan, menyeramkan.\n
bhikkhaka: m.  pengemis, peminta-minta, pendaduk (meminta-minta bukan karena miskin), petapa pengemis.\n
bhikkhati: minta sedekah, meminta(-minta).\n
bhikkhā: f.  makanan hasil mengemis, makanan dermaan, makanan; **~cariya**berkeliling untuk mengemis, berkeliling untuk mendapatkan derma makanan.\n
bhikkhu: m.  pengemis, peminta sedekah; rahib Buddha, bhikkhu.\n
bhikkhunī: f.  pengemis wanita, bhikkhuni, rahib Buddhis wanita.\n
bhitti: a.  dinding; **~khīla**m.  pasak dinding.\n
bhindati: membelah, memecahkan, menghancurkan, memutuskan, memotong, membongkar.\n
bhinna: (pp dari **bhindati**) pecah, hancur, terpecah belah, tak mufakat; dianalisa, terurai;  **~paṭa**kain sobek, kain perca; **~paṭadhara** mengenakan kain tambal seribu. [▶ bhinneka tunggal ika]
bhiyyo: (**bhīyo, bhīyyo**) a.  lebih (banyak); adv.  secara lebih (banyak, tinggi, besar), berulang-ulang, lebih jauh; **~bhāva**m.  lebih banyak, bertambah banyak, pelipatgandaan.\n
bhiyyoso: adv.  semakin; **~mattāya**amat sangat.\n
bhisa: nt.  tunas teratai, akar teratai, batang tanaman teratai, serabut teratai.\n
bhisi: f.  matras, jok, bantal, guling.\n
bhīru: a.  menakutkan, takut, takut-takutan, malu-malu, pengecut, mengerikan; m. ketakutan, kekecutan (hati); **~ttāṇa**nt. pernaungan bagi yang merasa takut; a. yang melindungi mereka yang merasa takut; yang terlindung dari ketakutan.\n
bhuñjati: makan, menyantap, menikmati, menggunakan, memanfaatkan; membersihkan, memurnikan.\n
bhutta: (pp dari **bhuñjati**) telah makan, telah disantap, makan, dia yang telah makan.\n
bhuttāvin: a. sehabis makan.\n
bhumma: 1. a.  berkaitan dengan bumi; nt. tanah, bumi, lantai; pl. **bhummā** yang ada di bumi, (= **bhumma-deva**) dewa-dewa yang menghuni bumi terutama dewa-dewa pohon (yakkha); tanah; 2. kasus lokatif.\n
bhummaṭṭha: a.  dimasukkan ke dalam tanah, terbenam dalam tanah, ditemukan di dalam atau di atas tanah, keduniawian; berdiri di atas tanah, terletak di atas tanah.\n
bhummattharaṇa: nt.  kain penutup lantai.\n
bhūta: a.  menjadi, terlahir, terbentuk, terwujud, nyata, riil;  nt. makhluk hidup; unsur (dasar), anasir; alam, dunia, yang ada; kebenaran, yang sejati, yang sebagaimana adanya; makhluk halus (hantu, puaka, raksasa, setan, dedemit); hal menjadi atau terjadi; **~pubba**a.  sebelumnya;  **~pubbaṁ**adv.  sebelum semua muncul, pada zaman dahulu kala, nun jauh sebelumnya; **~vejja(ka) ** m. dukun pengusir setan, dukun pengusir  roh jahat, dukun penyembuh kerasukan roh jahat.\n
bhūpati: m.  raja. [bupati ← Skt. bhūpati]
bhejja: a.  dibelah.\n
bheṇḍi: m.  sejenis peluru atau proyektil yang digunakan sebagai senjata; _panah_.\n
bhettar: m.  pemecah-belah.\n
bheda: m.  hal terurai, tercerai-berai, hancur, porak-poranda, terpecah belah; pelanggaran; jenis, macam; **dvādasavidhaākārabhedaṁ** terdiri dari dua belas jenis aspek; **bhedato** dibedakan dari. [beda ← Skt. bheda]
bhedana: nt.  hal memecah, membelah; penerobosan, pembagian, perceraian, pembongkaran, penghancuran; **~saṁvattanika** a. membawa (atau menuntun menuju) perpecahan atau perselisihan.\n
bhedeti (bhedāpeti): kaus.  dari **bhindati**.\n
bherava: a.  menakutkan, mengerikan, menciutkan nyali, menggentarkan.\n
bhesajja: nt.  obat, obat-obatan.\n
bho: (bentuk vokatif dari **bhavant**) kata sapaan akrab untuk orang yang sederajat atau lebih rendah; tuan, sobat, rekan, yang terkasih, Anda.\n
bhoga: m. penikmatan; milik, harta, kekayaan; lingkaran badan ular. [boga ← Skt. bhoga]
bhojana: nt.  makanan, santapan.\n
bhojaniya (bhojanīya, bhojaneyya): m.  apa yang dapat dimakan, makanan, yang layak untuk dimakan, makanan lunak, makanan utama, makanan pokok, makanan dasar, makanan primer.\n
bhojeti: (kaus. dari **bhuñjati**)  menyuguhi, menghidang, membuat menikmati.\n
maṁsa: nt.  daging;  **~pesi**f. potongan daging, gumpalan daging. [mangsa ← Skt. māṁsa]
makaci: m.  tanaman serat murva (_Sanseviera roxburghiana_).\n
makkaṭaka: m. laba-laba, kawa-kawa.\n
makkaṭī: f.  kera atau monyet betina.\n
makkhaṇa: nt.  pelumuran, pengolesan.\n
makkheti: mengolesi, melumasi, melumuri.\n
magga: m.  jalan, jalur, jalan setapak, titian. [marga ← Skt. mārga]
maṅku: a.  bingung, galau, terganggu, kacau, tidak senang atau puas.\n
maṅgala: a.  menguntungkan, makmur, beruntung;  nt. alamat baik, keberuntungan, berkah, tuah, yang mendatangkan kebahagiaan (keselamatan), sempena, tanda-tanda baik; selamatan, kenduri; tiga jenis pesta selamatan : **abhiseka~** (penahbisan, konsekrasi), **gehappavesana~**, **vivāha~**; _maṅgalaṁ karoti_  menyelenggarakan upacara pemberkahan, kawin; _maṅgalaṁ vadati_ memberkati. [manggala ← Skt. maṅgala]
maṅgula: a.  pucat, pudar, jelek.\n
maccu: m.  Dewa Kematian, Mara, kadangkala sama dengan Yama.\n
maccha: m.  ikan.\n
majja: nt.  minuman yang memabukkan, minuman keras, minuman beralkohol.\n
majjha: a.  tengah[an], antara, ugahari, setengah baya;  m.  pertengahan, pinggang. [madya ← Skt. madhya]
majjhaṇha: m.  tengah hari.\n
majjhatta: a.  “berdiri di tengah-tengah”, mewasiti, netral, tak berpihak, acuh tak acuh; keseimbangan batin.\n
majjhima: a. tengah, moderat, sedang, pertengahan, ugahari, tataran tengah; sedang, pertengahan; **~purisa** orang dengan perawakan sedang; orang kedua.\n
mañca: m.  ranjang, dipan.\n
mañcaka: m.  ranjang, katil, tempat tidur, peraduan, dipan, pembaringan.\n
mañjari (mañjarikā): f.  bunga bertangkai bercabang-cabang, tunas.\n
mañjūsā: f.  kotak (untuk menyimpan dokuman penting).\n
maññati: 1. berpikir, berpendapat, beranggapan, membayangkan, menganggap (sebagai); _yassa dāni tvaṁ, Raṭṭhapāla, kālaṁ maññasīti _ Sekaranglah waktunya, Ratthapala, lakukan apa yang Anda pikirkan; _taṁ kiṁ maññasi_ bagaimana pendapat Anda (mengenai ini); **maññe** kupikir, tentu saja, sungguh, saya kira, agaknya, kiranya, bisa jadi, tampaknya; _na maññe_ tentu saja tidak; 2. mengetahui, diyakini, yakin; bangga atas, angkuh, membanggakan.\n
maṇi: m.  batu mulia, batu akik, (batu) permata, manikam (intan; batu permata). [manik/manikam ← Skt. maṇi]
maṇḍana: nt.  hiasan, dandanan; **~jātika**yang bersifat (gemar akan) dandanan, gemar berhias.\n
maṇḍala: m.  lingkaran; diagram; bulatan matahari atau bulan; lempengan bundar; lingkup; kelompok, kalangan; sempadan jubah bhikkhu; kelim, pelipit, depun (kelim atau lipatan tambahan pada tepi kain atau pakaian sebagai hiasan); **= aṅgana **= lapangan, halaman, pelataran, medan, arena, gelanggang.\n
maṇḍalika: a. m.  penguasa wilayah, kepala daerah, adipati. [mandalika ← Skt. maṇḍalika]
maṇḍalikā: f.  lingkaran, bundaran, kawasan; **assa~** kawasan penggerombolan kandang kuda.\n
maṇḍeti: menghiasi, mendandani, memperindah.\n
mata: 1. (pp dari **maññati**)  terpikir, dipahami, dianggap; 2. (pp dari **marati**) mati; **~patika** a. menjanda. [mati ← Skt. mṛta/mṛti]
mati: f.  pikiran, pendapat, niat, kehendak, maksud, ide; kebijaksanaan, kecerdasan.\n
matta: 1.  a.  seukuran, sejumlah, sebanyak; hanya (_dassana mattam pi sādhu hoti_); seketika, karena, setara, seperti, seolah-olah, bagaikan; 2.  (pp dari **madati**) mabuk; gembira sekali atas, bangga akan, angkuh. [matra ←  Skt.  mātra]
mattikā: f.  tanah liat, lempung; lumpur.\n
matthaka: m.  kepala, puncak, ujung; **matthake** di kepala, pada jarak, di puncak.\n
mada: m.  1. kemabukan, berlebih-lebihan, pemuasan indriawi; 2. kesombongan, keangkuhan. [mada ← Skt. mada]
madana: nt.  kemabukan.\n
maddati: menginjak(-injak), melindas, menggilas, meremukkan; menaklukkan, menghancurkan; mengabaikan (sebuah nasihat), menolak, menampik; mencampurkan, mengadoni, menguli, meremas, meramas, mencampur-baurkan; mengirik (menginjak atau menebah agar terlepas dari tangkainya misalnya padi kering, kacang, dsb); merusak, menumbangkan (pagar); menarik atau menghela (jala).\n
maddita: (pp dari **maddeti**) dicampur-baurkan; diadoni; digilas, ditaklukkan.\n
madhu: m.  madu. [madu ← Skt. madhu]
madhura: a.  manis; memabukkan, membuai, menghanyutkan; nt. manis, minuman manis; pujian, sanjungan, hal menjilat.\n
manasi-karoti: menambatkan pikiran, mengarahkan pikiran, mencamkan, memikirkan, memperhatikan.\n
manasikāra: m.  perhatian, pemikiran, penambatan pikiran.\n
manāpa: a. menyenangkan, menawan hati, memesonakan, berkenan di hati, memikat (hati).\n
manussa: m. manusia.  [manusia ← Skt. manuṣya]
manesikā: f.  tebak pikiran.\n
mano: (**mana**) m. nt.  pikiran, batin, kesadaran. [_Mano_ merujuk ke fungsi intelektual dari kesadaran, _viññāṇa_ merujuk ke ranah indria dan reaksi indriawi, dan _citta_ merujuk ke aspek subjektif dari kesadaran.]
manda: a.  pelan, malas, lamban, kelesa, lembam, gial, celih, penyegar, menyenangkan; dungu, bodoh, bebal; seret; lembut (tentang mata atau tatapan); berbuah sedikit.\n
mamāyati: melekat pada, menggemari, mengandrungi, menginginkan; memelihara, merawat, menopang, menyayangi.\n
mamāyita: (pp dari **mamāyati**)  dipelihara, disayangi, disukai, diinginkan;  nt. kemelekatan, kegemaran akan, keangkuhan.\n
mamma: nt.  tempat lunak di tubuh, tempat yang vital (dalam Kitab Veda terutama merujuk ke bagian di antara tulang rusuk dekat hati; ulu hati), sendi; **~chedaka**menusuk hati, menyerang, menyakitkan.\n
maraṇa: nt.  kematian.\n
marati: mati; kaus. **māreti** membunuh; kaus. Pass.  **māriyati**ia (dibuat) terbunuh, ia dibunuh.\n
mariyādā: f.  perbatasan, batas, pantai, tepi laut, tanggul, pematang; hubungan yang digariskan atau diatur secara ketat, peraturan, kendali;  a.  menjaga agar tidak keluar jalur, mematuhi peraturan secara ketat.\n
mala: nt.  kotoran, noda, pencemar.\n
malaya: a.  berdebu.\n
masi: m.  jelaga, sulang, abu sisa pembakaran, tinta.\n
massu: m.  janggut, jenggot.\n
mahaggha: a.  sangat mahal, bernilai tinggi, berharga tinggi.\n
mahatta: nt.  kebesaran.\n
mahant: a.  besar, raksasa, luas, panjang lebar, agung, hebat. [maha ← Skt. mahant]
mahallaka: a.  besar, sepuh, senior, berusia lanjut. (_jātimahallakatāya samannāgate cirakālappasute vibhavamahantatāya samannāgate mahaddhane mahābhoge_)
mahāmatta: m.  menteri utama, perdana menteri, mahapatih.\n
mahāmegha: m.  awan tebal, awan petir, hujan besar.\n
mahāsāla: a.  memiliki balai besar (mewah), bergedung mewah.\n
mahiddhika: a.  gagah perkasa, digdaya, sakti, berilmu. [mahardika/merdeka ← Skt. mahārddhika]
mahī: f.  1. bumi, maha pertiwi; 2. nama sungai.\n
mahesī: f.  ratu, permaisuri.\n
mā: jangan, semogalah tidak; _māhevam  avoca _janganlah berkata demikitan.\n
māgavika: m.  pemburu, pemburu kijang (rusa).\n
māṇava: m.  remaja, anak muda, pemuda, Brahmana muda.\n
māṇavaka: m.  remaja, pemuda, Brahmana muda.\n
mātar: f.  ibu.\n
mātugāma: m.  wanita.\n
mātucchā: f.  saudara perempuan dari ibu; tante atau bibi dari pihak ibu.\n
mātumattin: a.  yang berhubungan dengan ibu, milik ibu, pihak ibu.\n
mādisa: a.  orang seperti saya.\n
māna: 1. m. keangkuhan, kecongkakan; penghormatan; 2. nt. ukuran; ukuran tertentu (satu **māna** = 8 **nāḷi**).\n
mānatta: nt.  sejenis penebusan kesalahan (dalam kaitan dengan pelanggaran sangghadisesa).\n
mānasa: nt.  niat, maksud, pikiran, hasrat.\n
mānita: (pp dari **māneti**)  dihormati, dimuliakan, diagungkan.\n
mānusa: a.  manusia(wi); m. manusia.\n
mānusaka: a.  manusia.\n
māneti: menghormati, menjunjung tinggi, memuliakan, mengagungkan, memuja-muja.\n
māpeti: membangun, mendirikan, menciptakan, membuat, menjelmakan (dengan kekuatan gaib).\n
māmaka: a.  terkasih, tersayang; pengikut, penggemar; **Buddha~**Buddha yang terkasih.\n
māra: m.  ‘sang pembunuh’, sang penggoda, Sang Jahat, Mara; kematian; (Ada lima jenis : _devaputta_, _kilesa_, _khandha_, _kamma_, _maccu_).\n
māraṇa: nt.  pembunuhan, kematian, pembantaian.\n
mārisa: a.  yang terkasih, tuan.\n
mālā: f.  untaian bunga, bunga-bunga, kalung atau karangan bunga; baris, rangkaian; **~vaccha** m. tanaman bunga hias, tumbuhan bunga hias.\n
māḷa: m.  bangunan dengan lantai atasnya berpuncak satu atau beratap bundar dan runcing.\n
māḷaka: 1. m.  ruang, bangunan; 2. = **mālaka** = **aṅgana** = **maṇḍala**m.  lapangan (yang terbatas), halaman, pelataran, arena, gelanggang, medan, alun-alun.\n
māsa: 1. m.  bulan; nama kedua belas bulan dalam setahun adalah _citta_ (_citra_), _vesākha_, _jeṭṭha_, _āsāḷha_, _sāvaṇa_, _poṭṭhapāda_, _assayuja_, _kattika_, _māgasira_, _phussa_, _māgha_, dan _phagguna_; awal tahun dimulai dari seputar pertengahan bulan Maret; 2. kacang hijau (_Phaseolus radiata / radiatus_), atau kacang _Phaseolus indica_. [masa ← Skt. māsa]
māsaka: m.  butiran kacang hijau yang digunakan sebagai standar berat dan nilai; mata uang bernilai rendah (1 **kahāpaṇa** = 4 **pāda** = 20 **māsaka**).\n
miga: m.  binatang buas, hewan jalang, binatang liar, meraga, marga; rusa, kijang, antelop, gazelle. [meraga, marga ← Skt. mṛga]
migī: f.  rusa betina.\n
micchā: salah, tidak benar, sesat, keliru.\n
mitta: m. nt.  teman, kawan, sahabat; **~āmacca** m. handai tolan. [mitra ← Skt. mitra]
middha: nt. kelambanan, ketidakcekatan, kelembaman.\n
miyyati:  (mīyati)  mati.\n
milakkhu(ka): m.  seseorang yang bukan dari kaum (suku) Ariya misalnya dari Andh(r)a, Tamil dan lain sebagainya; bahasa non-Ariya.\n
milāyati: melemah, mengendur, melayu, memudar, mereda; kaus. **milāpeti**mengeringkan, membuat layu, meredakan, menghilangkan, menekan, melumpuhkan.\n
missa: a.  tercampur dengan, beragam jenis, bersama, dibarengi dengan, diiringi dengan; yang terhormat.\n
missaka: 1. a. campuran, kombinasi; 2. m. pelayan, pengikut, abdi; 3. nt. nama sebuah taman hiburan di surga; 4. pl. sekelompok dewa.\n
missatā (missattā): f.  hal tercampur, tergabung.\n
mihita: nt.  senyum; ~pubba dengan senyum.\n
mukha: nt. mulut, muka (wajah), pintu masuk, lubang, depan (muka); alasan, cara, sebab, dengan cara. hebat; **mukhaṁ karoti** gerising (mengerot-erotkan muka), meringis, menyeringai; **~tuṇḍa(ka)**nt.  paruh, moncong; **~vaṇṇa**m. cahaya muka, air muka. [muka ← Skt. mukha]
mugga: m.  kacang merah (PED: _Phaseolus mungo_; KBBI: _P. vulgaris_).\n
muggara: m. gada, palu.\n
mucchati: menjadi kaku, membeku; menjadi tergila-gila; kaus. **muccheti** mengeluarkan suara, meninggikan suara.\n
mucchita: (pp dari **mucchati**) tak menyadarkan diri, (jatuh) pingsan; bingung sekali, kegila-gilaan.\n
muñcati: melepaskan, membebaskan; menanggalkan, memberikan, melontarkan, memancarkan, mengirim, mengeluarkan, melakukan, mengerjakan, melimpahkan, meninggalkan; pass. **muñcīyati, muccati**menjadi bebas, dibebaskan, dilepaskan.\n
muñciya: adv.  kecuali, terlepas dari.\n
muñja: m.  1. sejenis rumput atau ilalang (_Saccharum munja Roxb._); 2. sejenis ikan.\n
muṭṭha: (pp dari **massati**)  telah lupa, yang lupa; **~sacca** nt. suka lupa, kelengahan, kelalaian; **~ssati** a. lengah, lalai, suka lupa.\n
muṭṭhi: f.  tinju, kepalan tangan, genggaman.\n
mutta: 1. (pp dari **muñcati**) dilepaskan, dibebaskan, terbebas, dikorbankan; 2. air kencing, kemih, air seni, urine.\n
muttā: f.  mutiara.\n
mutti: f.  kebebasan, pembebasan, pelepasan.\n
muditā: f.  gembira (atas kebahagiaan pihak lain), hati yang lembut, simpati.\n
mudu: (**muduka**) a.  lembut, lunak, empuk, lentur; **~bhūta**a. lembut, lunak, empuk, lentur, gemulai. [merdu ← mṛdu]
muddha: (**muddhā**) m.  kepala, puncak.\n
musala: m. nt.  alu (penumbuk), godam, pentung, linggis (perejang).\n
musā: adv.  secara salah, tidak benar, tidak betul;  **~vāda**m. berbohong, kebohongan, dusta.\n
muhutta: m. nt.  saat, waktu yang sangat singkat, sekejap, sebentar, sejenak; **muhuttena**dalam sekejap, dalam waktu singkat.\n
mūga: a.  bisu, membisu
mūla: nt. akar, kaki, dasar, bawah, dekat; awal, pangkal, mula, sebab, alasan, sumber; pokok, tumpuan; dana, uang. [mula ← Skt. mūla]
mūlaka: a. disebabkan oleh, dengan muasal, berpangkal pada, berpokok pada; bernilai tertentu, berharga, dibayar mahal;  nt. = **mūla**.\n
mūḷha: (pp dari **muyhati**) tersesat, bingung, buta, dungu, bebal.\n
megha: m.  awan, mega, hujan. [mega ← Skt. megha]
mettā: f.  cinta kasih, keramahan, kehangatan. (SnA. _hita-sukhūpanaya-kāmatā_ keinginan untuk memberikan kemaslahatan dan kebahagiaan kepada pihak lain.)
methuna: a.  berkaitan dengan hubungan seksual; nt. hubungan seksual; m. sahabat.\n
methunaka: m.  pelaku percabulan, pelaku hubungan seksual, pezina; rekan;  nt. persetubuhan, percabulan.\n
meda: m.  lemak, gemuk.\n
medhāvin: a.  cerdas, pandai, bijak, bijaksana.\n
meraya: nt.  minuman beralkohol.\n
mokkha:  1. m. kebebasan, pembebasan, keselamatan, pelontaran, hal mengutarakan; 2. a. terdepan, pertama, terkemuka. [moksa ← Skt. mokṣa]
mokkhacika (mokkhacikā f.): m.  jumpalitan, jengkoletan, berjungkir balik.\n
mogha: kosong, sia-sia, tak berguna, bodoh, dungu
moceti: (kaus. dari **muñcati**) menghantarkan, membebaskan; mengeluarkan, melepaskan, memuncratkan, memelesat; menunaikan, memenuhi.\n
modaka: m.  1. sejenis manisan/halwa; 2. tempat surat, amplop, pembungkus atau sejenisnya.\n
mora: m.  merak. [merak ← Skt. mayūra/maura]
moha: m.  kebodohan, kedunguan, kegelapan batin, kekaburan kalbu, kebingungan, kelinglungan, delusi
ya: yang;  **yo yo**di mana saja; **yena yena gacchati**ke mana pun ia pergi.\n
yakkha: m.  nama sejumlah makhluk bukan manusia (_amanussa, mahiddhika peta_), misalnya makhluk halus, jin, hantu, mambang (makhluk halus yang menurut kepercayaan sebagian orang membinasakan manusia [bermacam-macam warnanya, ada yang kuning, merah, hitam, dsb] dan disebut juga menurut tempatnya misalnya ~segara, ~tali arus); gergasi (raksasa yang besar, suka makan orang), raksasa, buta.\n
yagghe  ~ jāneyyāsi: tahukah Anda….?
yajati: mengurbankan, memberi kurban, mempersembahkan kurban, memberi persembahan, memberi derma, berdana.\n
yañña: m. kurban (pujaan atau persembahan kepada orang halus dengan berbagai-bagai maksud); derma atau dana (kepada Sanggha atau bhikkhu); _yañño vuccati deyyadhammo_ (4 _paccaya_, _anna_, _pāna_, _vattha_, _yāna_, _mālā_, _gandhā_, _vilepana_, _seyya_, _avasatha_, _padīpeyya_; Nd^2 523).\n
yaṭṭhi: f.  1. tongkat, galah; 2. batang; 3. ukuran panjang, = **7 ratana**.\n
yato: adv.  dari mana; sejak, ketika, semenjak waktu itu, dikarenakan, karena; **yato …. ettāvatā** sebab …… sehingga.\n
yattha: adv.  di mana (pun), sebagaimana.\n
yatra: adv.  di mana (pun), karena; **yatra hi nāma** (kata seru penegas) sungguh, lantaran, bahwa, oleh karena itu.\n
yathā: sebagaimana, sehubungan dengan, sesuai dengan (_yathā kālaṁ_ sesuai dengan waktunya), se…. (_yathā sukhaṁ_ sesuka mereka); **yathā yathā** dengan cara apa pun, bagaimana pun juga; **~raddha** ( = **ālabdha**) secukupnya, sekenanya, tanpa bumbu, ala kadarnya; **~vajja** “seperti yang terkutuk”, menirukan orang cacat.\n
yathābhūta: a.  sebagaimana adanya; yang sesungguhnya, yang sejati, yang sesuai dengan kenyataan; nyata; sesuai dengan kebenaran.\n
yadā: adv.  ketika, saat; ( = **yasmiṁ samaye**).\n
yadi: jika, apabila, kalau; **yadi … atha kasmā** kalau … lantas mengapa; **yadi evaṁ … (tu)** walaupun … namun; **yadi va** atau; **yadi evaṁ**kalau begitu, baiklah kalau demikian.\n
yama: 1. m. pengendalian (diri); 2. m. penguasa alam arwah (kematian); kematian; peta, arwah; 3. m. nt. sepasang, kembar.\n
yava: m.  barli (_Hordeum vulgare_).\n
yaso (yasa): nt.  kemasyhuran, ketenaran, reputasi, nama baik (harum), kemuliaan, keagungan, keberhasilan, kedudukan tinggi, status; (menurut Dhammapāla) hal memiliki banyak pengikut dan pelayan (_ayasoti parivāra-vipatti; parammukha-garahā vā_ Pac.A. 4:903).\n
yasmā: adv.  sebab, karena.\n
yahiṁ: ☞  **yattha**
yāgu: f.  bubur.\n
yācaka: a.  yang meminta, memohon.\n
yācati: memohon, meminta, memohon dengan sangat.\n
yādisa: a.  yang seperti, yang sebagaimana, apa saja, apa pun; _yādisaṁ kīdisaṁ dānaṁ_ derma apa pun.\n
yāna: nt.  hal pergi, menapak maju, sarana pergerakan, wahana, kendaraan, kereta; jalan (menuju).\n
yāpanīya: a.  sesuai atau cukup untuk menunjang kehidupan seseorang.\n
yāpeti (yapeti): (kaus. dari **yāti**) pergi, berada; membuat pergi, membuat seseorang pergi menuju, membawa menuju, menuntun menuju; bisa (terus), maju, bergerak, aktif; membuat jalan terus, melanjutkan atau meneruskan (hidup atau jalan); hidup dengan.\n
yāma: m.  pengendalian; waktu jaga, penggal waktu jaga malam (4 jam), penggal waktu malam hari; penghuni alam Dewa Yama (pl.).\n
yāva kīvañca: sejauh.\n
yāvajīvaṁ: adv.  seumur hidup.\n
yāvataka: a.  sebanyak, sejauh, apa pun, semua.\n
yāvadatthaṁ: adv.  sejauh yang dibutuhkan; sebanyak yang disukai;  a.  cukup, lumayan; banyak.\n
yāvadeva: hanya sekadar.\n
yuga: nt.  kuk dari suatu bajak atau kereta; sepasang, pasangan; generasi, masa; **~naddha**m.  pemasangan kuk pada, penggandengan, pemaduan; a. berpadu, harmonis.\n
yujjhati: bertarung, berperang, berlaga, bertempur; _muṭṭhīhi yujjhati_  beradu tinju, bertinju.\n
yuñjati: memasang, merangkai dengan, melibatkan diri dalam, mengupayakan.\n
yutta: (pp dari **yuñjati**)  terpasang, tergandeng, terangkai dengan, dihubungkan dengan, merujuk ke, terlibat, (bidang) yang digeluti, diperlengkapi (dengan), tersedia, siap, mampu, pantas, cocok, cukup, sesuai, benar, karena, konjungsi; **~yoga** m. pengerahan usaha.\n
yuvan: m.  pemuda, anak muda, remaja.\n
yebhuyya: a.  banyak, dalam jumlah besar, kebanyakan (**yebhuyyena** kebanyakan, sebagian besar); sebagaimana yang terjadi, biasanya, ada kalanya, lazimnya (**na yebhuyyena** biasanya tidak, biasanya sama sekali tidak).\n
yoga: m.  1. kuk, pemasangan kuk; 2. kaitan dengan, pencantolan pada, hubungan (alamiah) dengan, persekutuan (dengan), pertautan dengan; 3. ikatan, kemelekatan; 4. usaha, upaya, perjuangan; 5. perenungan, konsentrasi, ketaatan, yoga; \\uf086 kekuatan (gaib), ilmu sihir, pengaruh, sarana, rencana (siasat); \\uf087 alat, perlengkapan, sarana, obat penawar. [yoga ← Skt. yoga]
yogi: m.  seseorang yang berjuang untuk melatih batin.\n
yojiya:  adv.  setelah memasang, mengaitkan, memadukan, menyatukan, mempengaruhi, mengenakan, menyiapkan, mengupayakan.\n
yojeti: (kaus. dari **yuñjati**)  membuat kuk terpasang, merangkaikan dengan, mengikatkan dengan, menyatukan, mengaitkan, memadukan, mengenakan, mempergunakan, memasangkan, menyiapkan, melibatkan diri, mengupayakan, berusaha menyelami; kaus. **yojāpeti**; pass. **yojīyati**.\n
yoni: f.  rahim, kandungan; asal muasal, cara terlahir, cara kelahiran (wujud), tempat terlahir, alam kelahiran; sifat.\n
yoniso: sampai ke asal muasal atau landasannya yakni secara menyeluruh, teratur, bijaksana, patut; **~manasikāra**m.  perhatian yang semestinya (kondisi ini muncul juga pada kusalacitta yang tidak disertai dengan paññā).\n
rakkhati: melindungi, menaungi, menyelamatkan, melestarikan; mematuhi, menjaga, memelihara, mengawal; menyimpan rahasia, menyimpan, mengamankan.\n
rakkhita: (pp dari **rakkhati**)  dijaga, dilindungi, dikawal, di bawah pengawasan, diselamatkan.\n
raṅga: m.  1. warna, cat; 2. panggung, pentas, teater, tempat murni, tempat (ruang) bermain.\n
racchā: f.  jalan kendaraan.\n
rajaka: m.  tukang celup, tukang kelantang.\n
rajata: nt. perak.\n
rajo (raja): nt.  debu, kotoran (biasanya basah, menghasilkan noda); noda, noktah, cemaran; **rajojalla** debu dan noda, kotoran lumpur.\n
rajja: nt. kerajaan, kekuasaan kerajaan, tahta, kedaulatan.\n
rajju: f.  tali. [rajut?]
raṭṭha: nt.  pemerintahan, kerajaan, negeri, negara, masyarakat.\n
ratana: nt.  batu mulia, permata, ratna, mestika; harta benda, kekayaan, benda bernilai. [ratna ← Skt. ratna]
rati: f.  cinta, kemelekatan, kesenangan, kegemaran akan, kesukaan akan.\n
ratta: 1. (pp dari **rañjati**) diwarnai, berwarna; merah (tua); bergemilau; terkelantang (= putih); bergairah; 2. nt. malam; waktu;**~ññu** lama, berjalan lama, berdiri lama, terkenal.\n
ratti: f.  malam.\n
ratha: m.  kereta beroda dua, bendi, _dokar_; pedati; kesenangan, kegembiraan. [rata ← Skt. ratha]
rathaka: 1. nt. kereta kecil, kereta mainan; 2. a. mempunyai kereta.\n
rathikā (rathiyā): f.  jalan atau jalur dokar atau pedati.\n
ramaṇīya: a.  yang sangat menyenangkan, menggembirakan, menawan hati, memikat, sangat menarik, memesonakan, bagus, elok, memukau.\n
ramati: menghibur diri, bersenang-senang, suka.\n
rava: m.  kecepatan, hal cepat sekali; suara nyaring, keras; pekik, teriakan, jeritan, lengking (hewan).\n
ravi: m.  matahari;  **~vāra**m.  Hari Minggu. [rawi Ü Skt. ravi]
rasa: m.  jus, sari buah, ekstrak buah (_ucchurasa _air sari tebu); rasa (subjektif dan objektif); cita rasa, yang nikmat atau hal menikmati, nuansa, sifat esensial atau fungsi (istilah dalam Abhidhamma), elegan, kecemerlangan, sari (_paṭhavīrasa _humus), ekstrak, substansi. [rasa ← Skt. rasa]
rassa: a.  pendek.\n
rahas (raho): nt.  tempat terpencil, terkucil, sendirian, rahasia, _tersembunyi_, pribadi; **rahogata** a. sendirian, secara pribadi, sedang menyendiri.\n
rahassa: a.  rahasia, tersembunyi;  nt.  kerahasiaan. [rahasia ← Skt. rahasya]
rāga: m.  warna, pewarna; nafsu (yang menggebu-gebu), renjana, berahi, nafsu ragawi; kemelekatan.\n
rājadhānī: f.  kota kerajaan.\n
rājā (rājan) :  m. raja, kaisar, penguasa, pangeran, (juga sebutan untuk kaum kesatria), pemimpin, hulubalang, pengawal raja. [raja ← Skt. rājā]
rāsi: m.  1.  gugusan, gabungan, himpunan, kumpulan, kelompok, kategori, (g)undukan, tumpukan,; 2. kekayaan, harta; 3. rasi (Ada 12 yakni _mesa_, _usabha_, _methuna_, _kakkaṭa_, _sīha_, _kaññā_, _tulā_, _vicchikā_, _dhanu_, _makara_, _kumbha_, _mīna_. [ram, bull, twins, crab, lion, virgin, balance, scorpion, bow, capricorn, waterpot, fish; kambing jantan, sapi jantan, kembaran, kepiting, singa, gadis, neraca, kalajengking, busur, makara/ kaprikornus, tempayan, ikan.])
riñcati: meninggalkan, tinggal pergi, melepaskan, menanggalkan, mengabaikan; pass. **riccati**.\n
ritta: (pp dari **riñcati**)  kosong, hampa, tanpa, bebas dari, sia-sia.\n
rukkha: m.  pohon.\n
ruci: f.  kecemerlangan, kebenderangan; kecondongan, kesukaan, kesenangan.\n
ruccati: mencari kesenangan dalam (lok.), senang me…., terjerumus atau hanyut dalam, memikirkan atau berniat; _mā rucci_  janganlah melakukan….\n
rūpa: nt.  bentuk, wujud, jasad, rupa, sosok, gambar, penampakan, perwujudan, objek; wujud jasmani; fenomena materi, materi (halus) (_rūpāvacara_ alam bermateri halus).  [rupa ← Skt. rūpa]
roga: m.  sakit, penyakit.\n
rogin: a.  berpenyakit, menderita penyakit.\n
rocati: menyenangkan, menggembirakan; senang atau gembira dalam; roceti  merasa senang atau gembira terhadap, senang terhadap, menerima dengan senang hati.\n
rodati: menangis, meratapi.\n
ropeti: (kaus. dari **rūhati**) 1. menanam, menempatkan, memasang, menumbuhkan, menambah, menumbuhkembangkan, mengatur, mengarahkan ke; 2. membuat terputus atau terpotong, menangguhkan, membatalkan, mengabaikan, menolak; membuat mengaku, mendakwa, menuduh.\n
lakkhaṇa: nt.  tanda, ciri, karakteristik, cena, sifat, kualitas, keistimewaan, seluk-beluk; pengenal; tanda badan; atribut khusus. [laksana ← Skt. lakṣaṇa]
lakkhika: a.  beruntung, penuh berkah; **alakkhika**a.  tidak beruntung, malang.\n
lagati (laggati): melekat pada, menempel pada, bergantung pada, tersangga pada, tersangkut pada.\n
laguḷa: m.  pentung(an), _gada_.\n
lagga: (pp dari **laggati**)  menempel, tersangkut, melekat, terhalang.\n
laggita: (pp dari **lagati**) tertempel pada, lekat pada, tergelantung pada, dihalangi, tersangga pada.\n
laṅghati: melanggar, melompat melewati, melangkahi; meremehkan, mengabaikan.\n
lajjin: a. merasa malu, santun sederhana, segan, sungkan, tidak madar (tidak berperasaan, tebal telinga), cermat berhati-hati.\n
lañchana: nt.  cap, tanda, tera, stempel; tanda mata, cendera mata, lencana. [lencana ← Skt. lañchana]
laṇḍika: f.  kotoran, tahi.\n
latā: f.  tumbuhan menjalar, sulur tanaman menjalar; sebutan untuk **taṇhā**; coreng, gores, kilasan. [lata ← Skt. latā]
laddha: (pp dari **labhati**)  telah memperoleh, mengambil, menerima.\n
lapati: berbicara, berujar, mengoceh, bergumam.\n
lapita: (pp dari **lapati**)  dibicarakan, diutarakan, diujar, berceloteh, bergumam.\n
labuja: m.  sukun (PED: _Artocarpus lacucha_ atau _incisa_; KBBI: _Artocarpus incissus_).\n
labbhati: (pass dari **labhati**) diperbolehkan, mungkin, bisa jadi, pantas, didapati.\n
labha: a.  menerima, diterima, mendapat.\n
labhati: mendapat, menerima, memperoleh, meraih; mendapat izin; mendapat kesempatan, diizinkan mendapat; kaus. **labbheti**; grd. **labbhiya**.\n
labbhā: mungkin, bisa saja.\n
lambin: a.  menggelantung, menjulur; beralat kelamin panjang menjulur.\n
laya: m.  jangka waktu yang singkat, sejenak, sebentar, _sejurus_, sekejap, sesaat; jangka waktu dalam musik, waktu yang sama, irama, ritme.\n
lasati: mendambakan, menginginkan; menari, memerankan, berpentas, berakting; berolahraga, memancarkan, menyuarakan; kaus. **lāseti**berolahraga, melakukan gerak badan, berhibur diri.\n
lahuka: a.  ringan, enteng, remeh, sepele.\n
lākhā: f.  lak, pewarna lak.\n
lābha: m.  pendapatan, laba,  perolehan, milik, kebaikan, keuntungan, kemaslahatan; **lābhena lābhaṁ**meraup laba dengan laba. [laba ← Skt. lābha]
lābhagga: a.  perolehan tertinggi; banyak perolehan materi.\n
lābhin: a.  menerima, mendapatkan, meraih, memiliki.\n
lāmaka: a.  remeh, jelek, buruk, jahat, inferior, nista.\n
lāyati: memotong, menyiangi, menuai.\n
likhati: menggores, memotong, mengukir, menulis, memoles, melicinkan.\n
likhita: (pp dari **likhati**) tergores, terpotong, diukir, dipoles; ditulis, dilicinkan, ditandai.\n
liṅga: nt.  sifat, tanda, ciri; penanda seksual, jenis kelamin; alat kelamin; penampakan, penampilan; **pul~** jenis kelamin laki-laki, maskulin; **itthi~** jenis kelamin wanita, feminin; **napuṁsaka~** jenis kelamin netral. [lingga ← Skt. liṅga]
limpati: mengolesi, memelester, menodai, melumuri; pass. lippati ternoda, tercemar.\n
līna: (pp dari **līyati**) melekat, menempel, lamban, lembam, melempem, pemalu, pendiam, suka menyendiri, menutup diri, senyap.\n
līyati: menempel, melekat; melumer, luput dari, terlepas.\n
luta: a.  terpotong.\n
luddaka: m.  pemburu.\n
luddha: (pp dari **lubbhati**)  keserakahan, ketamakan, lobha; kekejaman, kekerasan.\n
lubbhati: bersifat serakah, tamak, loba; mendamba-dambakan, menginginkan.\n
lūkha: a.  kasar, kasap, kesat; tak menyenangkan; jelek, buruk; cukupan, serba sedikit; (orang) nista, buruk sekali, kasar, menyedihkan, menjijikkan, lusuh, jembel, rusak, jorok, berpenampilan jembel berdisiplin keras; **~ppasanna** a. menaruh keyakinan pada orang yang jembel berdisiplin keras, menghormati orang yang berpenampilan lusuh. [rusak ← Skt. rukṣa]
lekha: m.  tulisan, huruf, surat.\n
leḍḍu: m.  sebongkah tanah; **~pāta** sepelemparan bongkahan tanah.\n
leṇa (lena): nt.  kamar, gua, ruang gua; penaungan, peristirahatan, keselamatan.\n
lepa: m.  pengolesan, pelumuran, penurapan (tembok), pelepaan; turap, lepa; hal melengket, melekat. [lepa ← Skt. lepa]
lesa: m.  pura-pura, dalih, helat, kilah, akal, muslihat.\n
loka: m.  dunia, penghuni dunia; **~uttara** a. di atas/luar keduniawian, adiduniawi. [loka ← Skt. loka]
loṇa: nt.  garam; a. asin; **~sovīraka**nt. bubur asam yang diberi garam; campuran dari aneka herba, aneka tanaman, aneka buah, aneka padi-padian, aneka kacang-kacangan, aneka daging, madu, gula, sendawa, garam, rempah-rempah, dan sebagainya; disimpan dalam tempayan selama dua sampai tiga tahun, digunakan sebagai obat.\n
lobha: m.  keserakahan, kerakusan, loba.\n
loma: nt.  bulu badan; **lomaṁ pāteti** tunduk; **~haṁsa**m. menggidikkan bulu roma; meremang, merinding, menyeramkan, seram (berdiri bulu roma). [roma ← Skt. roma(n)]
lomasa: a. berbulu (halus), ditutupi dengan bulu (halus), lembut.\n
lola: a.  terombang-ambing, penuh nafsu, serakah, tamak.\n
lolupa: a.  serakah, tamak.\n
loha: nt.  tembaga, _kuningan_, perunggu (gangsa), logam; loyang (tembaga kuning; kuningan; gangsa); **~kumbhī**f. cerek atau bejana logam; **~kaṭāha** wadah tembaga (atau kuningan).\n
lohita: a.  merah, merah darah; nt. darah.\n
vaṁsa: m.  1. bambu; 2. suku bangsa, wangsa, silsilah, keluarga; 3. tradisi, kebiasaan turun temurun; pemakaian, reputasi; 4. dinasti; 5. suling (bambu), seruling; \\uf086 suatu permainan; **~ñña **warisan turun-temurun yang luhur. [wangsa/bangsa ← Skt. vaṁsa]
vagga: 1. m. kelompok, grup, bagian, gugus; bab; 2. a. nt. tercerai-berai, terpisah-pisah, terkotak-kotak, tak utuh, tak rukun, berselisih. [warga ← Skt. varga]
vaggiya: a. kelompok, grup, gerombolan.\n
vaṅka: a. 1. melengkung, bengkok; 2. tidak lurus, tidak jujur; 3. meragukan, mengecohkan, menipu; m. lengkungan; kait; kail ikan.\n
vaṅkaka: nt.  bajak (luku, tenggala) mainan.\n
vacana: nt.  ucapan, ujar, kata, tuturan, perintah, pernyataan (_vacanaṁ karoti_  menuruti perkataan, mengikuti nasihat); istilah, ungkapan; **eka~** tunggal; **bahu~** jamak. [wacana ← Skt. vacana]
vacanīya: a.  seyogianya dikatakan, disebut, dijawab, diberi tahu, dinasihati.\n
vacī: f.  ucapan, kata-kata.\n
vacca: nt.  tahi, berak, kotoran, tinja, feses; **~magga** anus, dubur.\n
vaccha: m.  1. pedet, anak sapi; 2. pohon.\n
vajja: 1.  nt.  yang harus dihindari, kesalahan, dosa; 2. a. nt. “dikatakan”, mengatakan; dibunyikan (musik), dimainkan; ucapan.\n
vajjati: 1. dihindari, disingkirkan dari; kaus. **vajjeti**menghindari, menjauhkan diri dari; 2. pass. dari **vadati**; _vutto vajjeti_ menyampaikan salam.\n
vañcati: berjalan-jalan; kaus. **vañceti**menipu, memperdayakan, mencurangi, mengelabui, melakukan tipu muslihat.\n
vañjha: a.  mandul.\n
vaṭaṁsa (vaṭaṁsaka): m.  sejenis hiasan kepala, bumban (karangan bunga atau daun-daunan sebagai perhiasan kepala).\n
vaṭṭa: a.  putaran, daur, bulat; nt. lingkaran; putaran kelahiran berulang-ulang; yang telah diajukan atau dikeluarkan, derma, pengeluaran (biaya); **~ūpaccheda**penghancuran (pemutusan) siklus kelahiran kembali.\n
vaṭṭaka: nt.  kereta, gerobak.\n
vaṭṭakā: f.  burung puyuh.\n
vaṭṭati: bergerak, dilakukan; pantas (untuk); kaus. **vaṭṭeti** menggerakkan, memutar, memelintir.\n
vaṭṭi: f.  sumbu; pembalut, penyelubung, pembungkus, lapisan, selaput, kulit, jangat; pinggir(an), tepi, keliling, lingkar; setrip, carik (helai), lingkaran pinggir; selongsong, kantong, polong, gumpalan, bola, gelindingan, semburan, tuangan.\n
vaḍḍhaki: m.  tukang kayu, arsitek, ahli bangunan (pembangun), tukang batu.\n
vaḍḍhati: bertambah, berkembang, tumbuh, menjadi banyak; kaus. **vaḍḍheti**menumbuhkan, menjalankan, mengamalkan, sibuk dengan, mengembangkan, memancarkan, mengadakan, membuat, memelihara, menyiapkan.\n
vaḍḍhana: a. nt.  1. bertambah, bertumbuh, berkembang; 2. gemar akan, melekat pada, mengamalkan, mempraktikkan; 3. hal merapikan; 4. mengabdi kepada, memperkuat; 5. sejenis busana.\n
vaṇa: m. nt.  luka, borok.\n
vaṇijjā: f. dagang, perdagangan.\n
vaṇṭika: a.  berbatang, bertangkai.\n
vaṇṇa: m.  warna, rona, penampakan luar, warna kulit, jenis, kasta, kecemerlangan, keelokan, hal memuji, alasan, kualitas; **~vant**a.  indah, cantik, elok, rupawan, adun-temadun. [warna ← Skt. varṇa]
vaṇṇita: (pp dari **vaṇṇeti**) dijelaskan, diulas; dipuji, disanjung.\n
vaṇṇeti: menjelaskan, menguraikan; memuji, menyanjung, mempersenangkan hati.\n
vata: 1. sungguh, lah, betapa, alangkah, benar-benar, tentu saja;  2. m. nt. kewajiban agama, brata (tindakan pengendalian diri), praktik, pengamalan, kaul, pematuhan, laku, berprihatin. [brata ← Skt. vrata]
vati: f.  pagar; pilihan; anugerah.\n
vatta: 1.  nt. yang dilakukan, yang berlangsung atau lazim; tugas, kewajiban, pelayanan, kebiasaan, fungsi; janji, kaul, kebajikan, ibadat, pengamalan; 2. nt.  mulut; 3. a. terbuka lebar.\n
vattati: bergerak, mulai, melanjutkan, terjadi, berlangsung, ada, berada, melakukan, berjalan.\n
vatti: berkata, berucap, menyebut.\n
vattī: a. yang memelihara, berlatih, menyebabkan berlangsung terus.\n
vattha: 1. nt.  kain, _busana_, pakaian; 2. (pp dari **vasati**).\n
vatthi: m. f.  kandung kemih (buah pelir); kemaluan wanita; pencucian perut.\n
vatthu: nt.  lokasi, tempat, landasan, lapangan, pelataran, lahan, tanah milik, kebun; objek, benda, milik, benda nyata, barang, harta, substansi; sebab, alasan, pijakan, dasar; pokok, topik, cerita, kisah, hal, kasus.\n
vatthuka: a.  bertempat, berlokasi, berlandasan; berlandaskan, bersifat atau bersubstansikan.\n
vadati: (**vadeti**) berkata, mengatakan, memberi tahu, menegaskan, menyampaikan, mengutarakan, mengemukakan.\n
vadha: m.  hal membantai, membunuh, membinasakan, menewaskan, mematikan, membasmi, mengeksekusi; hukuman
vadhaka: m.  pembunuhan, pembantaian; pembunuh.\n
vadhū: f.  menantu perempuan.\n
vana: nt.  hutan, rimba, jenggala; nafsu, berahi, gairah;  **~saṇḍa**hutan belantara. [wana ← Skt. vana]
vanappati (vanaspati): m.  pohon hutan, pohon kayu, pokok kayu (dikontraskan dengan tumbuhan terna).\n
vanta: (pp dari **vamati**)  dimuntahkan, yang telah memuntahkan; dilepaskan, dicampakkan, ditinggalkan.\n
vandati: menyalami dengan penuh hormat, menghormati, menyembah, bersujud, memuliakan, mengagungkan, memuja.\n
vandanā: f.  penghormatan, sembah.\n
vapati: 1. menaburkan, menanam; pass. **vappate** atau **vuppati**; pp. **vutta**; kaus. **vāpeti** atau **vapāpeti**menyuruh menaburi; 2. mencukur, menyiangi, memotong rumput, memotong.\n
vamati: memuntahkan, mencampakkan, melepaskan.\n
vambheti: menistakan, merendahkan, menghina, mencerca, memaki-maki, mengomel, memarahi, menghardik, mengutuk.\n
vaya (vayo)  : m. (nt.) usia, umur; _vayo anuppatta_berusia senja, uzur, rimpuh (_jātivuddhabhāvaṁ antimavayaṁ anuppatte pacchimavayaṁ anuppatte pacchima-vayo nāma vassasatassa pacchimo tatiyabhāgo_); hilang, kurang, aus, memudar, lenyap; **~gata** dalam usia tua. [bea/biaya ← Skt. vyaya]
vayha (vayhā): nt. f.  kendaraan, wahana, pembaringan yang mudah diangkut, _tandu_.\n
vara: 1.  a. unggul, bagus sekali, terbaik, mulia; nt. **varaṁ**lebih baik, terbaik, terunggul; 2. keinginan, harapan, permintaan, doa; _varaṁ dadāti_ mengabulkan harapan; _varaṁ gaṇhāti_  berharap, berkaul.\n
valañjeti: menyusuri, menjalani, mempraktikkan, mencapai, mengambil jalan; menggunakan, menghabiskan, melewatkan.\n
valāhaka: m.  awan, mega, gegana, mega mendung (awan hitam).\n
vali (valī):  f.  garis, lipatan, kerut, kernyut, keriput, kedut, gores, garit, baris.\n
vallī: f.  tumbuhan merambat, tanaman menjalar; jenis alang-alang yang digunakan untuk mengikat sesuatu.\n
vavatthapeti: menentukan, memastikan, menunjuk.\n
vasa: m. nt.  kekuasaan, kendali, kekuatan, pengaruh; **vasena** disebabkan, dikarenakan, sehubungan dengan, sesuai dengan, sebagaimana, dalam hal, dengan cara, berdasarkan kekuatan dari; _vasaṁ vatteti_ mengendalikan; _vase vattati_ dikuasai seseorang; _vase vatteti_ mengendalikan, menguasai.\n
vasati: berbusana, mengenakan pakaian; hidup, menetap, tinggal, berdiam, melewatkan waktu, menjalankan, mematuhi, mempraktikkan, melakoni.\n
vasala: a.  busuk, kotor, bedebah, hina, keji; m.  orang buangan, orang nista, orang celaka, keparat, jahanam.\n
vasanta: m.  musim semi.\n
vasika: a.  di bawah kekuasaan, dikarenakan; **kodha~** korban kemarahan; **taṇhā~** di bawah pengaruh haus-damba; **pucchā~** untuk menjawab pertanyaan;**mātugāma~** keranjingan wanita.\n
vasin: a.  menguasai.\n
vassa: m.  hujan, guyuran/taburan; tahun; air mani; **~āvāsa**m. hal berdiam di satu tempat saat musim hujan, hal hidup melewatkan masa musim hujan. [warsa ← Skt. varṣa]
vassāna: m. musim hujan.\n
vahatu: m.  banteng (gen. sing. **vahato**).\n
vā: (kadang-kadang dalam syair ditulis sebagai  **va**) atau; **vā ……. vā**baik….maupun.\n
vāka: nt.  kulit kayu; **~cīra**busana petapa terbuat dari kulit kayu; rajutan jangat kayu.\n
vākya: nt.  tuturan, ucapan, ungkapan, kalimat, klausa, wacana.\n
vācā: f.  kata, ucapan, tuturan, perkataan;  _vācaṁ_ _bhindati_ memodifikasi ucapan atau ungkapan, mengatakan. [baca ← Skt.vācā]
vāṇija: m. pedagang, saudagar, niagawan.\n
vāta: m.  angin; **~pāna**m. kisi-kisi jendela, jendela; **~maṇḍalikā**f. angin puyuh, hembusan angin, angin topan, badai, angin taufan..\n
vāda: m.  perkataan, ucapan, pembicaraan, tuturan, ujaran, omongan, diskusi, perdebatan, perbantahan, pembahasan; doktrin, ajaran, paham, terori; .\n
vādaka: a.  doktrin, sektarian, sesat (bidah).\n
vādin: a.  berbicara, berkata, mencetuskan, menganut, berpaham, memeluk.\n
vādeti: (kaus. dari **vadati**) membunyikan, memainkan (alat musik), bermusik (bermain musik).\n
vānara: m.  monyet, kera.\n
vāpi: f.  kolam, waduk, tanki.\n
vāpita:  (pp dari **vāpeti**) ditaburi, ditanami; disiangi.\n
vāyati: 1. menenun, menganyam; kaus. **vāyāpeti** ( = **vināpeti**); 2. bertiup, menghembus, berbau.\n
vāyamati: berjuang, berupaya, berusaha.\n
vāyāma: m. daya upaya, usaha, perjuangan.\n
vāra: m. putaran, kesempatan, waktu, kejadian, ronde, babak; bab, bagian.\n
vāraka: m. pot, jambangan, kendi.\n
vāri: nt.  air.\n
vāritta: nt.  penghindaran, hal menjauhi.\n
vāreti: (kaus. dari **vuṇāti**) 1. mencegah, merintangi, menghambat; 2. meminang, melamar; kaus. **vārāpeti** membuat memperistri, membujuk seseorang mempersunting seorang istri; pp. **vārita**.\n
vāreyya: nt.  perkawinan, pernikahan, peminangan, pelamaran.\n
vāla: m.  bulu ekor; bulu kuda; bulu hewan; ekor; saringan bulu; **~ṇḍupaka**m. nt.  sikat bulu (kumparan/bantalan bulu) a.\n
vālikā: f.  pasir.\n
vāḷa: m.  ular; pemangsa, binatang buas pemangsa; **~yakkha** yakkha buas.\n
vāsa: 1. m. pakaian; 2. m. hidup, kehidupan, hal berdiam atau tinggal; rumah, kediaman; keadaan, kondisi; 3. parfum, wewangian.\n
vāsi: f.  pisau tajam, ka(m)pak, beliung (kapak bermata melintang).\n
vāsin: a.  berbusana, dibalut, mengenakan; berdiam di, bertempattinggalkan.\n
viṁhita: a. tercengang, membuat takut, menakutkan.\n
vikattana: nt.  pemotong, pisau.\n
vikāra: m.  perubahan, yang berubah, distorsi, pengembalian (pembalikan), pemutarbalikan, kelainan, pemberbedaan, gerak isyarat (sikap, kial); _vikāraṁ karoti_  berkial.\n
vikāla: m.  “waktu yang salah”, bukan pada waktunya; (terlalu) telat (atau kasip); sangat malam; silam.\n
vikirati: mencerai-beraikan, menghamburkan, menyebarkan, mengacau-balaukan atau mengaduk-aduk.\n
vikopeti: mengguncang, mengusik, mengganggu, merusak, menghancurkan, memusnahkan, membunuh, membinasakan.\n
vikkiṇāti: menjual
vikkhambhati: menjadi kaku (karena takut), ketakutan.\n
vikkhambhana: nt.  meruntuhkan, menghentikan, melumpuhkan, mengikis, membuang.\n
vigata: a.  lenyap, enyah, hilang, musnah, tanpa, bebas dari.\n
vigarahi: memarahi (dengan pedas), mencaci-maki, _mengecam_.\n
viggaha: m.  percekcokan, pertengkaran, perselisihan, yang berwujud, wujud, badan, sosok; pemenggalan kata-kata ke dalam unsur-unsurnya; analisis.\n
viggahita: (pp dari **viggaṇhati**)  digenggam, dicengkeram, ditangkap, berprasangka terhadap, tersandera, tergoda oleh.\n
vighāsa (vighasa): m.  sisa-sisa makanan, serpihan daging.\n
vicāra: m.  penyelidikan, pengamatan, pemantauan, pemindaian, berkutat, memenungkan.\n
vicāreti: (kaus. dari **vicarati**)  mengedarkan, membuat berkeliling, membagi, mendistribusi; memikirkan, merenungkan; menyelidiki, mencermati, menguji; merencanakan, merancang, membangun; melakukan, merawat, memelihara, mengelola, menyediakan.\n
vicikicchā: f.  keragu-raguan, kesangsian, sikap skeptis.\n
vicitra: a.  beraneka ragam, beragam, berhiasan, berdekorasi, berornamen.\n
vicinati (vicināti): menyelidiki, memeriksa, mencermati, memilah-milah; mencari, memilih.\n
vicchika: m.  kalajengking.\n
vijaṭeti: menguraikan (kekusutan), menyisir (sehingga rapi kembali); menjelaskan.\n
vijambhati: membangunkan, membangkitkan.\n
vijambhita:  (pp dari **vijambhati**) (ter)bangun, bangkit, timbul.\n
vijayati: menaklukkan, menguasai, menang atas.\n
vijahati: meninggalkan, menanggalkan, melepaskan.\n
vijānana: nt.  hal mengetahui, menyadari, mengenali.\n
vijāyati: menghasilkan, melahirkan, beranak, menimbulkan; kaus. **vijāyāpeti** menyebabkan melahirkan.\n
vijāyin: a.  subur, mampu beranak.\n
vijita: (pp dari **vijayati**) takluk, tunduk, kalah; nt. tanah taklukan, wilayah, kerajaan.\n
vijjati: (pass dari **vindati**)  ditemukan, diketahui, eksis, ada.\n
vijjā: f.  pengetahuan, pengetahuan sejati, pemahaman, pengertian; ilmu; **~dhara** m. ahli mantra atau jampi-jampi; tukang sihir. [widya ← Skt. vidyā]
vijjhati: menusuk, melubangi, menembusi, memanah, menghantam, menggebuk, menetak, membelah.\n
viññatti: f.  isyarat, pemberitahuan, informasi; hal memberi isyarat.\n
viññāṇa: nt.  kesadaran.\n
viññāta: (pp dari **vijānāti**) telah mencerap, dikenali, diketahui, dipahami, direnungkan, dipelajari.\n
viññāpeti: memberitahu, menyampaikan, mengajarkan, mewejang, membuat mengerti, menyerukan, memohon.\n
viññū: a.  cerdas, pandai, cakap, terpelajar, bijaksana, arif.\n
vitakka: m.  perenungan, pikiran, pengerahan batin atau pikiran, kecondongan batin, penempatan batin pada suatu objek, pengarahan pikiran pada.\n
vitakketi: merenungkan, bernalar, memikirkan, merencanakan.\n
vitaccheti: menyobek, mencabik, merenggut; meratakan, melicinkan.\n
vitudati: menghantam, menusuk, menghunjam, menumbuk, mendorong, menabrak, menyerang.\n
vitta: m.  harta kekayaan, milik.\n
vitthāra: m. rentangan, lebar, lintang; rincian, panjang lebar.\n
vitthārita: (pp dari **vitthāreti**) dirinci, diuraikan, dibeberkan, dibentangkan.\n
vitthāreti: menyebarkan, merentangkan, membentangkan, mengembangkan, membeberkan, menguraikan.\n
vidahati: mengatur, menunjuk, menetapkan, menentukan, menyediakan, mempraktikkan.\n
viddesa (videssa): m.  permusuhan, kebencian.\n
viddhaṁsaka: m.  pembinasa, penghancur, pemusnah.\n
viddhaṁsati: berjatuhan, tercerai-berai, dihancurremukkan.\n
viddhaṁsana: nt.  hal meremukkan, menghancurkan, melenyapkan; a. menghancurkan.\n
viddhaṁseti: (kaus. dari **viddhaṁsati**) menceraiberaikan, menghancurkan.\n
vidha: a.  macam, jenis, ragam.\n
vidhamati: (**vidhameti**) menghancurkan, meluluhlantakkan, memorakporandakan, merusakkan, menceraiberaikan, membuat berjatuhan, membuat terpusing-pusing, memberantakkan.\n
vidhāna: nt.  perencanaan, pembangunan, hal melakukan, pelaksanaan, proses; upacara, ritual; penempatan, pengaturan, penentuan; penggantian.\n
vidhutika: m.  rangkaian bunga berbentuk lingkaran, untaian bunga, tandan bunga.\n
vinaya: m.  penyingkiran, _pengenyahan_; tata peraturan, tata tertib, tata laku; winaya, tata krama para bhikkhu, penanggalan, pelepasan.\n
vinā: tanpa, terpisah, tercerai.\n
vinābhāva: m.  perpisahan.\n
vināsa: m.  hal menjadi binasa, hancur, lenyap. [binasa ← Skt. vināśa]
vinicchaya: m.  pembedaan, perbedaan, pikiran, pendapat (kukuh), pemahaman penuh atas; keputusan; penyelidikan, pengadilan, pertimbangan; uraian rinci; penjelasan.\n
vinicchināti (vinicchinati, vinicchati)   : mengkaji, menyidik, mencoba, memutuskan.\n
vinidhāya: menyesatkan, mengaburkan, menyamarkan, memelesetkan.\n
vinipāta: m.  keruntuhan, kehancuran; tempat penuh penderitaan, yang ditimpa penghukuman, yang jatuh dalam alam celaka; alam celaka.\n
vinipātika: a.  akan terlahir di alam celaka.\n
vinibbhujati: memisahkan, menceraikan, membedakan; membengkokkan, membalikkan.\n
vinīvaraṇa: a.  tidak dirintangi, tak terhalangi, tak terbias, tidak berprasangka.\n
vineti: menyingkirkan, melepaskan, menanggalkan; menuntun, memandu, memberi instruksi, mengajari, melatih, mendidik.\n
vineyya: setelah menyingkirkan, menanggalkan, meninggalkan; a. cocok untuk dilatih.\n
vindati: mengetahui, menemukan, mendapatkan, mengenali, memiliki, menikmati, mengalami, meraih.\n
vipateyya: akan langsung  terpenggal, hancur berkeping-keping.\n
vipariṇata: a.  berubah, terjungkir, bejat, menyimpang.\n
vipariṇāma: m.  perubahan (memburuk), hal terjungkir.\n
vipallāsa: m.  penjungkiran, pembalikan, pengubahan, kesemrawutan, kekeliruan, distorsi.\n
vipassaka: a.  sanggup menilik secara terang atau jelas, merenungkan, mahir dalam mawas diri.\n
vipassati: menilik secara terang atau jelas, memiliki pandangan terang, melihat dengan jernih melalui batin, memiliki intuisi atau daya penilikan batiniah.\n
vipassanā: f.  penglihatan yang jernih dan mendalam, wipassana.\n
vipāka: m.  buah, berbuah, hasil, akibat.\n
vipāceti: menjadi terusik, mengeluh, menyebarluaskan.\n
vipula: a.  luas, banyak, berlimpah, besar.\n
vippakata: (pp dari **vippakaroti**)  dilakukan secara tidak sempurna, dikerjakan secara salah, terbengkalai, terhenti, terputus, belum selesai dikerjakan.\n
vippakaroti: menganiaya, memperlakukan dengan kasar.\n
vippakāra: m. perubahan.\n
vippakiṇṇa: (pp dari **vippakirati**)  ditaburi, diperciki (dengan), dikepung; berserakan di sana-sini, tercerai-berai.\n
vippakirati: menaburi, menghancurkan, mengacaubalaukan.\n
vippaṭipajjati: salah jalan; berbuat salah, keliru, khilaf; berbuat dosa, berbuat tidak senonoh.\n
vippaṭisārā: m.  penyesalan, sesal.\n
vippaṭisārin: a.  sesal, penuh penyesalan, menyesal.\n
vippayoga: m. hal berpisah dengan, perpisahan.\n
vippasanna: a.  murni, jernih, bersih, bahagia, cerah, suci.\n
vippasīdati: menjadi bersinar, jernih, puas, bahagia.\n
vibbhamati: berkelana, mondar-mandir, menjadi tersesat, kesasar, meninggalkan Sanggha, balik kembali (ke rumah meninggalkan Sanggha), memisahkan diri (dari Sanggha).\n
vibhaṅga: m.  pembagian, pembedaan, klasifikasi, pemilahan.\n
vibhajati: membagi(-bagi), membagikan, memilah-milah, merinci, menganalisis, mencerai-beraikan.\n
vibhatti: f.  bagian, kategori, ragam, kelompok, rincian; infleksi, deklensi, konjugasi.\n
vibhāga: nt.  pembagian, klasifikasi, uraian, pemilahan, pembedaan.\n
vibhāvayati: menjadi terang/gemilang, menjelaskan.\n
vimati: f.  keragu-raguan, kebingungan, kekhawatiran.\n
vimuccati: terbebas, dibebaskan.\n
vimuñcati: membebaskan, memancarkan.\n
vimutta: (pp dari **vimuñcati**) terbebas.\n
vimutti: f.  kebebasan, pembebasan, pemancaran, yang terlepas (dari).\n
vimokkha (vimokha): m.  pembebasan, kebebasan.\n
vimocaya: m.  terbebas, tiada melekat.\n
viya: seperti, sebagaimana, bagaikan, laksana; partikel keragu-raguan ; _na viya maññe_ saya kira tidak; **~bhāva**m. berkurang, mengecil.\n
virati: f.  (= **veramaṇī**) hal menghindari, menahan diri dari, menjauhkan diri dari; (tiga _virati_: _sampatta_, _samādāna_, dan _setughāta_ DA i 305; versi lain DhsA 154 _tisso viratiyo_).\n
viramati: berhenti, berpantang, menjauhkan diri, menahan diri.\n
viravati: berteriak, memekik, menjerit; berderik-derik, berderak-derak, berciut-ciut, berdesak; kaus. **virāveti**membunyikan.\n
virahita: a.  kosong, tanpa, bebas dari, tiada.\n
virāga: m.  tanpa nafsu, hal berpaling dari, tiadanya (lenyapnya) minat terhadap, tak berhasrat, hal pudar, murni, bersih dan bebas; kearahatan; _pītiyā ca virāgā upekkhako ca vihāsiṁ_ berpaling dari kegiuran (batin) dan berdiam dalam keseimbangan batin.\n
viriya: nt.  “keadaan seorang nan perkasa”, giat, semangat, aktif berupaya.\n
virūḷha: (pp dari **virūhati**)  setelah tumbuh, tumbuh.\n
virūḷhi: f.  pertumbuhan.\n
virūhati: tumbuh, bertunas.\n
virecana: nt.  obat pencuci perut, pencahar.\n
virocati: memancar, menyinari, menjadi cemerlang.\n
virodha: m.  rintangan, hambatan, lawan.\n
vilagga: a.  menempel, ramping, tersangkut.\n
vilapati: omong kosong; meratapi.\n
vilīva (viliva): a.  terbuat dari bilah (bambu); bilah (bambu dsb); **~kāra**m. perajin bambu, pembuat keranjang. [bilah ? ← Skt. bilma]
vilumpati: merampas, menjarah, mencaplok, mencuri, memusnahkan.\n
vilepana: nt.  urap, boreh (bau-bauan untuk melumasi badan supaya harum), kosmetik (bahan untuk mempercantik).\n
vilokita: (pp dari **viloketi**)  nt. memandang ke belakang, berpaling ke belakang.\n
viloketi: menyeksamati, memeriksa, mempelajari, mencermati, merenungkan.\n
vivaṭa: a. tersingkap, terbuka, telanjang; sadar dan jernih, cerah batin.\n
vivaṭṭakappa: m.  pembentukan kembali dunia, pertumbuhan dunia ( = **vaḍḍhamāno**).\n
vivaṭṭati: tergelar; memulai lagi; melenceng dari.\n
vivadati: bertengkar, cekcok, berselisih, berbantahan.\n
vivarati: membuka, menyingkapkan, membuat jelas, menganalisis; kaus. **vivarāpeti**menyingkap, membuka.\n
vivāda: m.  pertengkaran, percekcokan, perselisihan, perbantahan, pertentangan.\n
vivāha: m. nt.  “mengirim atau membawa pergi” (= **kaññādānaṁ** memberi atau menyerahkan anak gadis); perkawinan.\n
vivicca: (setelah) menjauhkan diri dari; jauh dari, menjauhi, membebaskan diri dari, mengasingkan diri.\n
viveka: m.  pelepasan atau pemisahan atau penjauhan (diri); penanggalan; penyepian, pengasingan diri; penyendirian; pengucilan, pembebasan, bebas.\n
viveceti: memisahkan, memilahkan, membedakan, mengkritik.\n
visa: nt.  racun. [bisa ← Skt. viṣa]
visaṁyoga: m.  bebas dari belenggu, pemisahan diri, pemutusan ikatan.\n
visaṁvādeti: memperdaya dengan kata-kata, mengingkari kata sendiri, ingkar, menipu, berdusta, berbohong.\n
visakkiyadūta: m.  utusan atau kurir khusus, utusan atau kurir yang tak sanggup (mampu).\n
visaṭṭhi: f.  pengeluaran, hal mengeluarkan; mendambakan, melekat.\n
visabhāga: a.  berbeda, berlainan, tak biasa, luar biasa, tidak umum.\n
visama: a.  tak rata, tak sama, tak serasi, berlawanan; tak sesuai, salah; ganjil, aneh, tak pantas; nt. tempat yang tak rata, bahaya, atau sulit dijangkau; jalan yang sulit ditapaki; ketidakrataan, keburukan, perilaku salah, ketidakpantasan; **visamena** dengan cara yang salah.\n
visaya: m.  tempat, wilayah, dunia, alam, daerah, lingkungan; jangkauan, rentang, medan, cakupan, ranah objek, objek, sifat, objek indra, kesenangan indriawi.\n
visahati: mampu, berani.\n
visāraka: a.  menyebar, merentang, memuai, mengembang, melebar, melantur, meluas.\n
visārada: a.  percaya diri, mantap, tidak canggung, bijaksana, terampil, mahir, tidak kikuk, tanpa sungkan.\n
visiṭṭha: a.  menonjol, kontras, luar biasa, dominan, kentara, mencolok, superior, lebih unggul.\n
visuṁ: secara terpisah, tersendiri; visum visum  masing-masing, satu per satu; **visukaraṇa** nt. pemisahan.\n
visuṁgāma: m.  tanah perdikan.\n
visuddha: (pp dari **visujjhati**)  bersih, murni, suci, jernih, bening, cemerlang, tiada noda. [wisuda ← Skt. visuddha]
visuddhi: f.  kecemerlangan, semarak, kemegahan, keunggulan; kemurnian, kesucian, penyucian; kebajikan.\n
visūka: nt.  gerakan yang tiada henti-hentinya, geliat-geliut, pelintir, puntiran, pertunjukan. (=**vipphandita**)
visūcikā: f. penyakit kolera.\n
vissa: a.  semua, setiap seluruh, segenap; nt. bau daging mentah; dunia; **~dhamma** Dhamma duniawi.\n
vissajjana:  (**vissajjanā** f.)  nt.  pemberian, penyerahan, pengeluaran, pengiriman, pelontaran; jawaban.\n
vissajjeti: (kaus. dari **vissajjati**) mengeluarkan, mengirim, menyingkirkan, melonggarkan, melepaskan, memberikan, menyerahkan; menjawab, menyahut.\n
vissasati (vissāseti) :  memercayai, bersahabat dengan, berkarib.\n
vissāsa: m.  kepercayaan, keakraban, kekariban, persetujuan bersama.\n
vissuta: a.  terkenal, termasyhur.\n
vihata: (pp dari **vihanati**)  dibunuh, dimusnahkan, dipukul, dilumpuhkan, berakhir; lebar.\n
vihanati: memukul, membunuh, mengakhiri, menghabisi, mengenyahkan.\n
viharati: hidup, berdiam, bersemayam, berada, singgah, berkunjung. [ = _iriyati, vattati, pāleti,  yapeti, yāpeti, carati_]
vihāra: m.  hal melewatkan waktu, berdiam di suatu tempat, hidup, tinggal, berada; tempat tinggal, berdiam,menghuni; keadaan kehidupan, kondisi, gaya hidup; kediaman, pondok, gubuk, hunian, kamar tunggal; tempat tinggal atau pernaungan pribadi bhikkhu untuk masa wassa (**vassāvāsa**) tempat pertemuan para bhikkhu, tempat istirahat atau hiburan; bangunan yang lebih besar untuk tempat para bhikkhu; wihara (semula merujuk ke gubuk, lalu berkembang menjadi sederetan kamar tinggal pribadi yang dihubungkan dengan sebuah beranda atau pamukha). [biara/wihara ← Skt. vihāra]
vihārin: a.  berdiam, tinggal, hidup, berada.\n
vihita: (pp dari **vidahati**) a.  tersusun, yang telah disiapkan, disediakan, dilengkapi, ditentukan
viheṭheti: menganiaya, menyusahkan, mengganggu, menyakiti, mendongkolkan.\n
vīta: a.  bebas dari, tanpa.\n
vītikkama: m.  melampaui, melanggar, melewati, berjalan, berlangsung.\n
vītināmeti: membuat melewatkan waktu, menghabiskan waktu, hidup, melewati, menunggu.\n
vītivatta: a.  setelah melewati atau mengatasi, ditembusi, terlewati.\n
vītisāreti: menyampaikan, saling menukar (ucapan salam), beruluk-salam.\n
vīmaṁsati (vīmaṁseti): “mencoba memikirkan”, mempertimbangkan, memeriksa, mencermati, menemukan, menyelidiki, mengkaji, menguji, menelusuri, merenungkan, menjajaki.\n
vīmaṁsā: f.  pertimbangan, pemeriksaan, pengujian, percobaan, penyelidikan, uji-coba; _iddhipāda_ yang ke-4
vīsati: f.  dua puluh.\n
vīhi: m.  beras merah, beras coklat, beras pirang.\n
vuccati: (pass. dari **vatti**)  disebut.\n
vuṭṭhahati (vuṭṭhāti: ) bangkit, terbit, dihasilkan; muncul dari, keluar dari, kembali dari.\n
vuṭṭhāpeti: (kaus. dari **vuṭṭhahati**)  menahbiskan, merehabilitasi, bangkit dari, keluar dari, berpaling dari.\n
vuṭṭhi: f.  hujan.\n
vuṭṭhika: a.  ada hujan.\n
vuṭṭhita: (pp dari **vuṭṭhahati**)  keluar (dari), bangkit dari, terbit, sekembali dari, tinggal pergi.\n
vuḍḍha (vuddha)  : (pp dari **vaḍḍhati**) tua, sepuh, uzur, jompo, renta, rimpuh, berida (_aṅgapaccaṅgānaṁ vuddhimariyādappatte sīlācārādiguṇavuddhiyutte_); **~vaya**usia tua.\n
vuḍḍhi: f.  pertumbuhan, perkembangan, kemajuan, kemakmuran; kedewasaan; **~ppatta** a. sudah dewasa.\n
vutta: 1. (pp dari **vatti**) dikatakan; 2. (pp dari **vapati**) ditaburkan (biji/benih); dicukur.\n
vutti: f.  tingkah laku, gaya, gaya hidup, praktik, penggunaan, kebiasaan.\n
vuttha: (pp dari **vasati**) telah berdiam, tinggal atau hidup.\n
vuddha: ☞  vuḍḍha
vuddhi: ☞  **vuḍḍhi**
vusita: (pp dari **vasati**) sudah berdiam, terpenuhkan, tersempurnakan sudah, terlakoni.\n
vūpasanta:  (pp dari **vūpasammati**) damai, kalem, tenang, hening, reda.\n
vūpasama: m. peredaan, pemadaman, pengenyahan, penenangan, penanggalan, penguasaan atas; hal menjadi reda, tenang, terkuasai, terkendali, lenyap, tersingkir.\n
vega: m.  cepat, sigap, impuls, kekuatan, kecepatan; **vegena **(=**vegasā**) adv. dengan cepat.\n
vejja: m. dokter, penyembuh, tenaga medis; **~kamma** nt. praktik pengobatan.\n
vejjikā: f.  praktik pengobatan.\n
veṭha: m. pembungkus, pembalut, lilitan.\n
veṭhana: nt.  sekeliling, seputar; serban, ubel-ubel, ikat kepala, tutup kepala; pembungkus, pakaian, selendang, syal.\n
veṇi: f.  kelabang atau kepang; seikat atau selampit rambut.\n
vetta: nt.  ranting, tangkai, benda yang menjalar, rotan.\n
vedanaṭṭa: a.  dilanda kesakitan.\n
vedanā: f.  perasaan, sensasi; sensasi sakit, penderitaan, kesakitan (_dukkhavedanā_).\n
vedayita: (pp dari **vedeti**)  dirasakan, dialami.\n
vedalla: nt. bunga rampai, salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**).\n
vedita: (pp dari **vedeti**)  dialami, dirasakan, dimaklumi.\n
vedeti: merasakan, menangkap, mencerap, mengalami (**vediyati**).\n
venayika: m.  seorang nihilis; ahli dalam winaya, terampil dalam winaya, orang mampu mengekang atau mengendalikan diri, orang yang terkekang atau terkendali.\n
vepurisikā: f.  wanita berwujud pria (misalnya berkumis dan berjanggut), wanita yang secara seksual seperti laki-laki, banci.\n
vepulla: nt.  perkembangan penuh, tergenapkan; hal berlimpah, banyak, penuh, kelimpahan; hal membesar, meruak.\n
vematika: a.  merasa ragu-ragu, merasa sangsi, tidak pasti, bimbang.\n
veyyākaraṇa: m. nt. jawaban, penjelasan, pemaparan; salah satu ragam kitab suci (▶ **navaṅgabuddhasāsana**);  m. orang yang ahli dalam menjelaskan atau menjawab, seorang ahli tata bahasa.\n
veyyāvacca: nt.  pelayanan, perhatian; kerja, pekerjaan, tugas, kewajiban.\n
vera: nt.  kebencian, perseteruan, permusuhan.\n
verañjā: f.  nama sebuah kota.\n
velā: f. waktu, kala, saat; pantai; (per)batas(an), batasan, kendali; tumpukan, kumpulan.\n
veḷu: m.  bambu, buluh, aur. [buluh ← Skt. veṇu]
vevacana: nt.  sebutan, julukan, sinonim.\n
vesī (vesiyā): f.  wanita berkasta rendah; pelacur; **~dvāra** bordil, rumah pelacuran.\n
vessa: m.  orang yang berkasta waisya. [waisya ← Skt. vaiṡya]
vehāsa: m.  penyangga; udara, langit, surga; hal berkalang atau melayang di udara.\n
vo: 1. kata partikel penekan, mungkin = **eva**; 2. bentuk enklitik dari **tumhe**; bentuk Ak. Ins. Dat. dan Gen. dari **tuvaṁ** (**tvaṁ**).\n
vokāra: m.  perbedaan; unsur pembentuk makhluk hidup yakni khandha (**eka~**, **catu~** dan **pañca~bhava**); hal yang sepele, tak berharga; gangguan, kesulitan.\n
votthapana (voṭṭhapana): nt.  hal menetapkan, menentukan; **~kicca**nt. hal berperan untuk menetapkan.\n
vodāna: nt.  hal membersihkan, membuat putih bersih; kemurnian, pemurnian, penyucian.\n
voropeti (oropeti): mencabut, menghilangkan, membuang; _jīvitā voropeti_ mencabut nyawa.\n
voharati: mengungkapkan, menegaskan, menetapkan, memutuskan, memerintah, mengelola; pass. **vohariyati** dipanggil.\n
vohāra: m.  perkataan, penyampaian, **kappiya~** perkataan yang sesuai; perdagangan, bisnis; ungkapan umum, istilah umum; dialek; tuntutan hukum, dakwaan, hukum, kewajiban hukum, praktik hukum, ilmu hukum; nama sejenis monster laut yang menawan perahu.\n
vohārika: m.  yang berkaitan dengan tuntutan hukum, hukum, kehakiman, hakim.\n
vyaggha: m.  harimau, macan (_Felis tigris_).\n
vyañjana: nt.  sifat, ciri, tanda; karakteristik (**purisa~** penis); huruf (dari suatu kata) (**vyañjanato**secara harafiah); bumbu, rempah-rempah, kari, lauk.\n
vyatta: a.  berpengalaman, ulung, pandai, piawai, terpelajar, bijak, cermat, bijaksana.\n
vyanta: a.  tersingkir, terpencil; nt. ujung, akhir.\n
vyantibhavati: berhenti, berakhir, musnah, binasa, lenyap.\n
vyasana: nt.  kemalangan, musibah, malapetaka, keruntuhan, kehilangan, kesengsaraan.\n
vyākaroti: menjelaskan, menjawab; meramalkan.\n
vyāpajjha: a. nt.  kesusahan, gangguan, disakiti.\n
vyāpāda: m.  hal menjahati, niat jahat.\n
vyābādheti (byābādheti): menganiaya, menyakiti, mengganggu, melukai.\n
vyūha: m.  tumpukan, deretan, pajangan.\n
vyūhati (viyūhati): berdiri berderet-deret; berpajang, mengambil, membawa pergi, memindahkan, menyingkirkan.\n
sa: 1. itu, ia, dia; 2. bahwa, bahwasanya (_sā’haṁ dhammaṁ nāssosiṁ_ bahwa saya tidak mendengar Dhamma); jika, kalau begitu, maka, sungguh, begitu (_sa kho so bhikkhu ….  upakkileso ti iti viditvā …. upakkilesaṁ pajahati _begitu ia mengenali…).\n
saṁyamati: mengamalkan pengendalian diri;  kaus. **saññāmeti**mengendalikan, mengekang.\n
saṁyācikā: f.  memohon, minta, yang diminta; **saṁyācikāya**adv.  dengan meminta bersama, dengan mengumpulkan sumbangan sukarela.\n
saṁyoga: m.  ikatan, belenggu; persatuan, perkumpulan; hubungan (dalam suatu kalimat), susunan atau bentuk.\n
saṁyojana: nt.  ikatan, belenggu.\n
saṁvaṭṭakappa: m.  kehancuran dunia, peleburan dunia ( = **parihāyamāno**).\n
saṁvaṭṭati: tergulung; mengalami kehancuran, berakhir, musnah.\n
saṁvaṇṇana: nt.  pemujian, pujian.\n
saṁvaṇṇeti: memuji-muji, menyanjung.\n
saṁvattati: menuntun menuju, mengarah pada, bermanfaat untuk, membuat, mengakibatkan.\n
saṁvattanika: a.  membawa, mendatangkan, menghasilkan, mengakibatkan, sering mengalami.\n
saṁvaddhana: nt.  hal bertambah, bertumbuh, berkembang.\n
saṁvara: m.  pengendalian, pengekangan, pemahaman.\n
saṁvarati: mengendalikan diri, memegang, mengekang.\n
saṁvāsa: m.  tinggal bersama, hidup bersama; persekutuan, kekariban, hubungan seksual, kumpul kebo, sepenghunian.\n
saṁvigga:  (pp dari **saṁvijjati**) tergugah, risau karena takut, dengan hati yang bergolak.\n
saṁvidahati: berunding, berkoordinasi, berembuk, memutuskan, menetapkan, menyediakan, menyiapkan, menyajikan, membereskan, menyelesaikan.\n
saṁvidahana: nt.  pengaturan, penyusunan, perencanaan, penetapan, janji; ketentuan, syarat; koordinasi.\n
saṁvidhāvahāra: m.  pencurian terencana; pencurian melalui persekongkolan.\n
saṁsagga: m.  kontak, sentuhan, hubungan, persatuan, pertautan, penyambungan.\n
saṁsaraṇa: nt.  arus, aliran; tirai geser, kerai (bidai) yang dapat disingkirkan.\n
saṁsarati: bergerak atau berpindah terus menerus; datang berulang-ulang, terlahir berulang-ulang.\n
saṁsāmeti: (kaus. dari **saṁ** + **ṡam**) “memuluskan”, melipat (tikar pembaringan), (_senāsanaṁ saṁsāmetvā  _merapikan peristirahatan).\n
saṁsāra: m.  perpindahan, hal terus menerus berjalan atau bergerak, peredaran, kelahiran berulang-ulang, samsara. [sengsara ← Skt. saṁsāra]
saṁsibbita:  (pp dari **saṁsibbati**)  terlilit, terjalin.\n
saṁsīdati: tenggelam, hanyut dalam (terpikat akan); tembus.\n
saṁhara: m.  mengumpulkan.\n
saṁhita: (pp dari **sandahati**)  berkaitan, dilengkapi dengan, memiliki, membawa.\n
sauttara: a. memiliki sesuatu yang melebihinya.\n
sauddesa: a.  dengan penjelasan, dengan (pe)rinci(an), dengan nama sebutan.\n
saka: a.  sendiri; _sakaṁ te_  semuanya milik Anda (salam untuk raja).\n
sakaṭa: m. nt.  kereta, _gerobak_.\n
sakadāgāmin: a. **☞sakadāgāmī**
sakadāgāmī: m.  yang akan kembali sekali lagi (terlahir sebagai manusia), yang telah mencapai tingkat kesucian kedua.\n
sakala: a. semua, seluruh, segenap.\n
sakasaṭa: a. salah, tidak benar, keliru.\n
sakid ( = sakiṁ): adv.  sekali.\n
sakuṇa: m.  burung.\n
sakuntaka: m.  sejenis burung, sejenis burung hering.\n
sakka: 1.  m.  Dewa Sakka, pemimpin para dewa di surga _Tāvatiṁsa_; 2. m. orang dari suku Sakya.\n
sakkacca(m): (ger. dari **sakkaroti**)  adv.  dengan hormat, takzim, cermat, serius, respek.\n
sakkata: (pp dari **sakkaroti**)  dihormati, diperlakukan atau dilayani dengan layak.\n
sakkaroti: menghormati, menghargai, memuliakan, respek terhadap, menerima keramahtamahan.\n
sakkā: (indekl.)  mampu, bisa, mungkin.\n
sakkāya: m.  adanya badan atau diri; **~diṭṭhi** f.  pandangan bahwa ada suatu diri pada badan ini atau salah satu dari gugusan badan ini, ilusi adanya suatu diri.\n
sakkāra: m.  keramahtamahan, hormat, sembah.\n
sakkuṇeyyata: nt.  kemungkinan, kebolehjadian.\n
sakkoti: mampu, sanggup.\n
sakkharā: f.  (batu) kerikil, kerikil kecil (batu lada); pecahan barang tanah; bijian, butiran; hablur, kristal; gula pasir; batu (hitam/asah).\n
sakkhali (sakkhalikā): f.  1. lubang telinga; 2. sejenis kue (basah) atau manisan/halwa; penganan; kudapan.\n
sakkhi:  yang (melihat) dengan mata sendiri, sebagai saksi, yang mengalami sendiri; _sakkhiṁ karoti_ menyaksikan dengan mata sendiri, minta (seseorang/genetif) bertindak sebagai saksi;  **~diṭṭha** a. menyaksikan dengan mata sendiri. [saksi ← Skt. sākṣī]
sakyaputta: m.  putra kaum Sakya.\n
sakyaputtiya: m.  siswa atau pengikut putra kaum Sakya.\n
sakhila: a.  ramah, bersahabat, menyenangkan.\n
saguṇa: a.  berpadu, bersatu, bertakak (terjadi dari dua helai); _saguṇaṁ karoti  _menakak.\n
sagotta: m.  sanak, kaum, marga.\n
sagga: m. surga, yang terang benderang. [surga ← Skt. svarga]
saṁkaḍḍhati: mengumpulkan; mencermati, memeriksa.\n
saṅkati: meragukan, menimbulkan kecurigaan.\n
saṅkappa: m.  pikiran, niat, kehendak, maksud, rencana, pengerahan pikiran. ( = **vitakka**)
saṅkama: m.  lintasan, jembatan, titian.\n
saṁkamati: menjelajahi, melintasi, berpindah, mengoper, mentransfer, mengalihkan, menapak, melangkah, melimpahkan.\n
saṅkampati: bergetar, berguncang, menggegar, menggelatar, bergoyang.\n
saṅkasāyati: menjadi lemah, bersiap, tunduk terhadap.\n
saṅkassara: a.  yang meragukan, bobrok.\n
saṅkāmeti: (kaus. dari **saṅkamati**) melewatkan, membuat pergi ke, memindahkan, menggeser, mengganti, menukar; datang atau muncul bersama-sama.\n
saṁkiṇṇa: (pp dari **saṅkirati**)  a.  tercampur, tidak murni, penuh dengan; bingung, berdesakan.\n
saṅkiya: a.  mencurigakan, cemas.\n
saṁkilesa: m.  noda, kotoran, pencemar (lawan dari **visuddhi**).\n
saṁketa: m.  isyarat, persetujuan, perjanjian, tempat yang ditetapkan, tempat berkumpul; _saṁketaṁ gacchati_  mematuhi perjanjian, datang ke pertemuan;  **asaṅketena** tanpa penetapan tempat;  **~kamma**nt.  persetujuan, permufakatan. [sengketa ← Skt. saṅketa]
saṅkha: m.  1. (kulit) kerang, keong/siput besar, lokan, giwang (siput mutiara); 2. sejenis tanaman air; **~likhita** terpoles atau mengkilap seperti kulit kerang (siput mutiara), laksana kulit kerang nan gemilap; cemerlang, sempurna. [sangka ← Skt. saṅkha]
saṅkhaya: m.  kemusnahan, kelenyapan, sirna, pengakhiran.\n
saṇkhalikā: f.  rantai.\n
saṅkhā: f.  pembilangan, penghitungan, penaksiran; bilangan; tentuan, definisi, kata, nama; _saṅkhaṁ gacchati_  dirumuskan, dikatakan, disebut, dimaksud, dibilang; _saṅkhaṁ na upeti (nopeti)_ tak dapat disebut sebagai, tidak dihitung sebagai, tidak dianggap sebagai, tidak dapat ditentukan sebagai.\n
saṅkhāta: (pp dari **saṅkhāyati**)  disepakati sebagai, dihitung sebagai, dianggap, dinamai, disebut.\n
saṅkhāyati: muncul; menghitung; ger. saṅkhāya  setelah mempertimbangkan, merenungkan, mencermati.\n
saṅkhāra: m.  1. pl. semua (fenomena-fenomena) yang berkondisi (_citta_, _cetasikā_, _rūpa_); _aniccā vata saṅkhārā_; 2. faktor-faktor mental, bentuk-bentuk mental (batin), yang meliputi seluruh cetasika kecuali perasaan (_vedanā_), dan persepsi (_saññā_); salah satu dari lima _khandha_ (agregat atau kumpulan) kemelekatan; unsur pembentuk; 3. niat, _sañcetanā_, _abhisaṅkhara_, _kamma_, sebagai faktor kedua dalam dua belas mata rantai _paṭicca-samuppāda_; faktor penggerak; pendorong; kekuatan (gaya); faktor pembentuk (segala sesuatu).\n
saṁkhitta: (pp dari **saṅkhipati**)  ringkas, singkat; tidak terpusat, melantur, tanpa perhatian; mengerut, tipis, mengecil, ramping, lampai, langsing.\n
saṅkhepa: m.  penyingkatan, ringkasan, ikhtisar, intisari, rangkuman; kumpulan, himpunan, kelompok, gundukan, tumpukan, timbunan; **saṅkhepena** adv. seakan-akan, seolah-olah, bagaikan.\n
saṅgacchati: berkumpul bersama, datang berkumpul, bertemu dengan; ger. **saṁgamma**.\n
saṅgaṇikā: f.  pergaulan, pergerombolan, sosialisasi, persekutuan.\n
saṅgaṇhāti: terdiri dari, mencakup, meliputi, mengumpulkan, berisikan, , merangkum, mengandung, menyingkatkan, memperlakukan dengan ramah (simpatik), bersimpati dengan, menyokong, berkenan, menolong, melindungi, merangkul.\n
saṅgaha: 1. m. hal mengumpulkan, berkumpul, merangkul; kumpulan, cakupan, kelompok; rangkuman, risalah, koleksi (Kitab Suci); keramahtamahan, bantuan, simpati, tindakan (perbuatan) simpatik; _saṅgahaṁ gacchati_  terdiri dari, termasuk, tercakup dalam; 2. nt. pengendalian, rintangan, ikatan.\n
saṅgahita (saṅgahīta)  : (pp dari **saṅgaṇhāti**)  terdiri dari, meliputi, mencakup, terangkul, tercakup, terkandung, termasuk, terkelompok, terkumpul, terangkai, terangkum, terangkul, tergolong, terkekang, terkendali, berniat baik.\n
saṅgāma: m.  pertarungan, pertempuran, peperangan. [senggama ← Skt. saṅgāma]
saṅgāmeti: bertarung, bertempur, berperang dengan.\n
saṅgāyati: melantunkan, menguncar, menuturkan kembali.\n
saṅgāyana: nt.  hal melantunkan, menguncarkan, menuturkan kembali; Konsili Buddhis.\n
saṅgāhaka: a.  mengumpulkan, merangkul, merangkum, melakukan perbuatan simpatik; sais.\n
saṅgha: m.  kumpulan, rombongan, persamuhan, peguyuban; sanggha, persamuhan para bhikkhu.\n
saṅghaṭṭana: nt.  (f. **saṅghaṭṭanā**)  hal beradu bersama, kontak, tabrakan, persenggolan, pembenturan.\n
saṅghāṭī: f.  jubah luar (berlapis ganda), sangghati.\n
saṅghāta: m.  hal menghantam, membunuh, memperadukan, memetik (jari); pengumpulan, kumpulan, agregat; nama dari salah satu dari delapan neraka utama.\n
sace: jika, apabila, kalau.\n
sacca: a.  benar, betul; sebetulnya, sesungguhnya; nt. kebenaran, alasan. [setia ← Skt.  satya]
saccavādin: a.  yang selalu mengatakan yang sebenarnya, jujur.\n
sacchikaroti: menyaksikan sendiri; mewujudkan; mengalami sendiri. [saksi ← Skt. sākṣin]
sacchikiriyā: f.  realisasi, perwujudan, hal mengalami.\n
sajjita: (pp dari **sajjeti**)  dikirim, diberangkatkan, dilepaskan, dikeluarkan, diberikan, disiapkan, tercukupi.\n
sajjhāya: m.  pengulangan, penghafalan, belajar, mempelajari.\n
sañcaraṇa: nt.  hilir mudik, tempat pertemuan; lalu lintas.\n
sañcaritta: nt.  bolak-balik, bertindak sebagai perantara atau penghubung.\n
sañcalati: tak stabil, goyah, gual-gail, labil, gelisah; kaus. **sañcāleti**menggoyahkan, mengguncang.\n
sañcicca: adv.  dengan sengaja, dengan sadar, secara terencana.\n
sañcetanika: a.  dengan sengaja.\n
saṁcopana: nt.  hal menyentuh, menjamah, bergerak, penggerayangan, hal berkeliaran.\n
sañjānana: nt.  (**sañjānanā** f.)  hal mengetahui, mencerap, menangkap, mengenali; sifat, ciri.\n
sañjānāti: mengetahui, menyadari, menginsafi, mencerap; berpikir, menduga, mengira; memanggil, menyebut, menamakan, memberi nama panggilan.\n
sañjāyati: dilahirkan, dihasilkan.\n
sañjhā: f.  senja. [senja ← Skt. sandhyā]
saññā: f.  pengertian, kesadaran, pencerapan, persepsi, pengenalan, penyadaran; konsepsi, ide, gagasan, pikiran; tanda, isyarat, kesan, ingatan.\n
saññāpeti: (kaus. dari **sañjānāti**)  mempermaklumkan, memberi tahu, mengajar; memprotes, membantah, membujuk, meyakinkan, mengesankan, membuat terkesan; menenangkan, menenteramkan, mendamaikan.\n
saññin: a.  sadar, menyadari, menangkap, memiliki persepsi.\n
saṭṭhi: enam puluh.\n
saṭha: a.  licik, suka menipu atau mengelabui; m. tipuan.\n
saṇikaṁ: adv. perlahan-lahan, pelan-pelan, berangsur-angsur, dengan lembut.\n
saṇṭhapeti (saṇṭhāpeti): (kaus. dari **santiṭṭhati**) membereskan, mendirikan, menertibkan, mengatur, melipat (melempit).\n
saṇṭhāna: nt.  bentuk, susunan, posisi, sifat (dasar), wujud, rupa, penampakan; bahan bakar; peristirahatan, balai pertemuan, ranah publik (pasar).\n
saṇḍa: m.  onggokan, kumpulan, rumpun, belukar.\n
saṇḍāsa: m.  pinset, penjepit, capit, sepit, angkup.\n
saṇha: a.  mulus, lembut, halus; sopan, santun, ramah.\n
sata: a.  ingat, waspada, eling, awas, penuh sati, sadar; nt.  seratus;  **~padī**f. lipan, halipan, kelabang; **~sahassa**nt. seratus ribu.\n
sataṁ: bentuk gen. pl. dari “**sant**’, ‘_of the true ones_’ = **santānam**.\n
sati: f.  ingatan, keawasan, kewaspadaan, kesadaran (diri), batin nan terjaga, tak leka (dari), hal eling atau ingat, perhatian murni, _sati_ (_upaṭṭhitā sati_  batin yang awas, penuh sati, dengan eling, dengan sati tertegak).\n
satimant: a.  dengan sadar, dengan awas,waspada, eling, dengan penuh sati.\n
satta: a. 1. tujuh; [sapta ← sapta]; 2. (pp dari **sajjati**) melekat pada menempel pada; 3. (pp dari **sapati**) terkutuk, disumpahi;  m. makhluk hidup; jiwa; inti (substansi). [satwa ← sattva]
sattama: 1.  a. terbaik, terunggul, terhebat; 2. ketujuh, ke-7, VII.\n
satti: f.  1. kemampuan, kekuatan, kesaktian; 2. pisau, belati, pedang; tombak, _lembing_. [sakti ← Skt. ṡakti]
sattha: 1. nt. senjata (tajam), _pedang_, pisau; 2. nt. ilmu, seni, pengetahuan [sastra ← Skt. ṡāstra];3. karavan, kafilah; 4. (pp dari **sāsati**) diberitahu, diajari; 5. a. mampu, cakap, kompeten; \\uf086 bernapas.\n
satthar: m.  guru.\n
satthi: f.  paha.\n
sadā: adv.  selalu, senantiasa.\n
sadisa: a.  mirip, seperti, sama.\n
sadda: m.  suara, bunyi; kata (_ayaṁ hi pariyāya-saddo desanāvāra-kāraṇa vattati_); **~lakkhaṇa** etimologi; **~vidū**ahli tatabahasa. [sabda ← Skt.  ṡabda]
saddahati: mempercayai, meyakini.\n
saddha: a.  percaya, yakin, beriman; mudah percaya, mudah diperdayai; upacara pemakaman untuk menghormati keluarga yang telah meninggal dengan mempersembahkan makanan dan hadiah kepada para brahmana.\n
saddhamma: m.  Dhamma nan sejati, kebenaran atau ajaran yang sejati (sesungguhnya).\n
saddhā: f.  keyakinan, kepercayaan, iman; **~deyya** nt. pemberian atau derma atau persembahan berdasarkan keyakinan, manipulator keyakinan (theft of faith).\n
saddhiṁ: bersama-sama.\n
saddhivihārika: m.  rekan sepenghunian, rekan sesama bhikkhu; murid (dari **upajjhāya**), murid pendamping.\n
sanivāra: m.  Hari Sabtu.\n
sant: (ppr dari **atthi**)  1. ada, eksis; 2. baik, bagus, benar.\n
santa: 1. (pp dari **sammati**) tenang, kalem, damai, murni; 2. (pp dari **sammati**) lelah, capai, lesu, lunglai.\n
santaka: a.  1. milik; karena, lantaran; di bawah (kekuasaan), dalam lingkup; 2. terbatas, berhingga.\n
santati: f.  kesinambungan, kelangsungan, kontinuitas, proses, garis silsilah atau keturunan.\n
santappati: dipanasi, dibuat kesal; berduka cita, bersedih hati; kaus. **santappeti** membakar, menghanguskan, menyiksa; memuaskan, menyenangkan. [santap ?]
santāna: nt. (pen)jalaran, percabangan; sulur, carang; satu di antara lima pohon surgawi; kontinuitas, rangkaian, rentetan, silsilah.\n
santika: nt.  sekitar, seputar, dekat, di depan, dalam kehadiran, di hadapan.\n
santikā: f.  sejenis permainan; “_spellicans_“ atau “_spillikins_“.\n
santiṭṭhati (saṇṭhahati, saṇṭhāti): berdiri, berdiri diam, tetap, terus; muncul; ditegakkan, didirikan, ditertibkan, diatur; melekat pada, tertambat pada, berkukuh pada; menunggu, menantikan.\n
santuṭṭhi: f.  kepuasan, marem (puas hati, senang).\n
santuṭṭhitā: f.  keadaan puas.\n
santhata: (pp dari **santharati**) tersebar, bertaburan dengan, ditutupi, dilingkupi, berpelapis, terbentang, terentang, ditebar.\n
santharati: menebarkan, membentangkan, menutupi, melapisi; kaus. **santharāpeti**menyebabkan terbentang.\n
sandati: mengalir.\n
sandamānikā: f.  kereta pertempuran atau perang.\n
sandahati: menempatkan bersama, menghubungkan, menyusun.\n
sandiṭṭha: (pp dari **sandissati**)  tampak bersama, bersahabat, kenalan.\n
sandissati: tampak bersama, terlibat dalam, cocok dengan, bersesuaian dengan, hidup sejalan dengan, hidup seiring dengan;  kaus. **sandasseti**mengajar, mewejang, membandingkan, mencermati, memeriksa.\n
sandhāna: nt.  persatuan, persekutuan, persahabatan, ikatan, belenggu; menyatu berkesinambungan (manifestasi dari _citta_).\n
sandhāya: setelah dipadukan, sehubungan dengan, dengan merujuk pada, terhadap, berhubungan dengan.\n
sandhi: m. f.  penyatuan, perpaduan, penyambungan; lubang, penembusan, penerobosan; jurang; sambungan; gabungan; sandi. [sandi ← Skt. sandhi]
sannipatati: berkumpul, datang bersama-sama; kaus. **sannipāteti**mengumpulkan, mengadakan pertemuan; kaus. II  **sannipātāpeti**menyebabkan diadakan pertemuan atau dipanggil.\n
sannipāta: m.  penyatuan, perpaduan, kejadian yang kebetulan; orang-orang yang berkumpul, pertemuan, kumpulan, perkerumunan; kumpulan cairan lendir tubuh; sanding kata.\n
sannibha: a. mirip, seperti.\n
sannisajjā: f.  tempat pertemuan.\n
sannisinna:  (pp dari **sannisīdati**) duduk bersama, menjadi mapan.\n
sannisīdati: terduduk, mereda; kaus. **sannisādeti** menenangkan, meredakan; kaus II. **sannisīdāpeti** menghentikan.\n
sannissita: a.  berlandaskan, berdasarkan, berkaitan dengan, berhubungan dengan, bergantung pada, bersandar pada, ditopang oleh.\n
sapatta: m.  bermusuhan, lawan, rival, saingan, musuh bebuyutan.\n
sapattī: f.  _co-wife_; sesama istri.\n
sapadānaṁ: adv.  “dengan langkah yang sama” (tanpa sela); berkesinambungan, sinambung; _sapadānaṁ carati_  pergi berpindapata tanpa selangan atau bersela, berjalan dari rumah ke rumah.\n
sappa: m.  ular.\n
sappāya: a.  layak, bermanfaat, cocok, sesuai, pantas;  nt. sesuatu yang bermanfaat, menolong, manfaat; **~kiriyā** memberi obat.\n
sappi: nt.  gi, cairan mentega, mentega cair, mentega jernih, minyak samin; **~maṇḍa**kekat atau krim mentega jernih, kepala gi.\n
sappurisa: m.  orang yang baik, orang yang berguna. (= **ariya**)
sabala: a.  berbintik-bintik, bermosaik, beraneka ragam (warna).\n
sabba: a.  semua, seluruh, segenap, setiap; **sabbena** **sabbaṁ**segala-galanya, sama sekali; **~nāma**kataganti orang; **~lahusa** teringan.\n
sabbaññū: a. yang mengetahui semuanya; m. Sang Maha Tahu.\n
sabbattha: adv.  di mana-mana, dalam kondisi apa pun
sabbatra: ☞  **sabbattha**
sabbadā: adv.  selalu, senantiasa, setiap hari.\n
sabbaso: a.  menyeluruh, utuh.\n
sabrahmacarin: a.  rekan sepenghidupan suci.\n
sabhā: f.  balai, balai pertemuan; penginapan atau pemondokan umum (khalayak ramai), pesanggrahan.\n
sabhāga: a.  umum, sekelompok, sejenis, sama, mirip, seperti.\n
sama: m.  ketenangan, ketenteraman; kelelahan;  a.  sama, rata, datar; mirip, seperti, serupa; seimbang, tegak lurus, adil; sebanding, sama tengah; semuanya (**samatiṁsa** semuanya tiga puluh; tiga puluh secara keseluruhan; **samena**dengan adil; **samaṁ**sama(-sama). [sama ← Skt. sama]
samaka: a. sama; adv. secara sama.\n
samagga: a.  bersatu, serasi, rukun, akur, sebati (bersatu padu, sangat mesra, sesuai).\n
samaṅgin: a.  dianugerahi dengan, memiliki; **samaṅgībhūta**nt. memiliki, dilengkapi dengan; _samaṅgi karoti_  memperlengkapi dengan.\n
samacārin: a. hidup dalam kedamaian.\n
samaṇa: m.  ‘orang yang berdaya-upaya’, orang yang meninggalkan kehidupan berumah tangga dan hidup mengembara atau bertapa (di hutan) mengendalikan nafsu dan bermeditasi; _pertapa_.\n
samaṇaka: m.  petapa jahat atau hina; ‘sedikit mirip petapa’.\n
samatitthika: a. rata atau setinggi dengan tepian alias cukup penuh.\n
samatta: 1. nt. kesamaan, keseimbangan, keadilan; 2. a. selesai, tuntas, beres, kelar, lengkap, menyeluruh, sempurna.\n
samattha: a. mampu, kuat, berdaya.\n
samatha: m.  penenangan, ketenangan batin; peredaan; penyelesaian, pengendapan.\n
samanugāhati: menanyakan alasannya, menanyakan secara saksama, mendesak, mencecar, menyidik; ppr. med. **samanuggā-hiyamāna** didesak.\n
samanupassati: melihat.\n
samanubhāsati: berbicara, merundingkan, mempelajari bersama-sama, mengajak bicara, menasihati, _menegur_.\n
samanussarati: mengenang, mengingat.\n
samanta: a.  semua, seluruh, sepenuhnya, segenap, sekeliling, semua sisi; _samantā vesāliṁ_ seantero Wesali; _samantato nagarassa_ seluruh kota; **samāsamantato** segenap, di mana-mana.\n
samannāgata: a.  yang diikuti oleh, memiliki, yang dianugerahi dengan, yang disertai dengan, yang diliputi, yang penuh dengan.\n
samappita: (pp dari **samappeti**)  diserahkan, dikirimkan, diberikan; dianugerahi dengan, memiliki, dipengaruhi, memiliki sifat.\n
samappeti: menyampaikan, memberikan, mengirimkan, melakukan, menaruh.\n
samaya:  m. saat; kala; kondisi; konggregasi (himpunan); perkumpulan; musim; kesempatan; akhir. [Menurut Buddhaghosa, _samaya_ mempunyai sembilan arti : (1) _samavāya_ (hal berkumpul, berjumpa bersama); (2) _khaṇa_ (kesempatan); (3) _kāla_ (musim atau waktu; _saradasamaya_); (4) _samūha_ (massa, gerombolan); (5) _hetu_ (kondisi); (6) _diṭṭhi_ (pandangan atau pendapat); (7) _paṭilābha_ (perolehan); (8) _pahāna_ (pengenyahan atau penanggalan); (9) _paṭivedha_ (penembusan).\n
samassasati: dibuat segar; kaus. **samassāseti** menenangkan, meringankan, menyegarkan, melegakan.\n
samāgacchati: bertemu bersama, berkumpul, masuk dengan, bersua, pergi, melihat.\n
samācāra: m.  perilaku, tingkah laku, sepak terjang, kelakuan, tindak-tanduk.\n
samādapeti: membuat atau menyuruh mengambil, menggugah, menghasut, mendorong, membangkitkan.\n
samādahati: mengumpulkan, memusatkan (pikiran), memasuki samadhi; tenang, menyalakan.\n
samādāna: nt.  hal mengambil, membawa, menjalankan, mengamalkan, bertekad, berjanji.\n
samādiyati: mengambil untuk dijalankan, menjalankan, mematuhi, mengusung, mengamalkan, berikhtiar, berupaya; **samādāya vattati**berikhtiar dan mempraktikkan.\n
samādisati: menunjukkan, memerintahkan, menyuruh.\n
samādhāna: nt.  menempatkan bersama, menyandingkan, menambatkan, terpusat, konsentrasi, selaras, serasi.\n
samādhi: m.  konsentrasi (pikiran/batin); samadhi. [semadi ← Skt. samādhi]
samādhiyati: pass. dari **samādahati**.\n
samāna: sama, mirip; ada, hadir; sejenis dewa;  **~upajjhāya**upajjhaya bersama-sama.\n
samānatta: a.  seimbang, setara, kebersamaan.\n
samānattatā: f.  keseimbangan, kesetaraan, kebersamaan, sehidup sependeritaan (sepenanggungan).\n
samāpajjati: mencapai, memasuki; menjadi, terjadi; mewujudkan, menjelmakan, melakukan, membuat terjadi.\n
samāpatti: f. pencapaian; tingkatan atau taraf meditasi.\n
samāpana: nt.  dorongan, hal tergugah, tergerak.\n
samāpanna: (pp dari **samāpajjati**) setelah mencapai, tiba pada, memasuki, bergabung dalam.\n
samāpeti: menyelesaikan, membereskan, menuntaskan, mengakhiri.\n
samāyoga: m.  penggabungan, penyatuan, penjalinan.\n
samāhita: (pp dari **samādahati**)  tenang, mantap, terkendali, terpusat; telah mencapai; yang telah diletakkan/dipasang. (_samāhitattā eva ca ekaggaṁ acalaṁ nipphandaṁ_)
samiñjati: membekuk, menekuk (melipat), digerakkan, diguncang.\n
samukkheṭita: a.  dinistakan, dicampakkan.\n
samugga: m. kotak, keranjang.\n
samugghāta: m.  pencabutan, penghapusan, penyingkiran, pengakhiran, peniadaan.\n
samucchindati: mencabut sampai ke akar-akarnya, memotong, melenyapkan, menghancurkan, menanggalkan.\n
samucchinna: a.  tercabut, terpotong.\n
samuṭṭhahati: timbul, muncul; kaus. **samuṭṭhāpeti** memulai, mengemuka, timbul.\n
samuṭṭhāna: nt.  kemunculan, sebab.\n
samuttejeti: menggairahkan, menggembirakan, penuh dengan antusiasme.\n
samudaya: m.  hal muncul, asal-muasal, asal mula; pancaran, pancuran; hasil pendapatan.\n
samudāgama: m.  awal, timbul, hasil; **samudāgamato paṭṭhāya** pertama-tama.\n
samudācarati: berlaku, dipraktikkan, diterapkan, berlangsung, terjadi; memperlakukan; berbicara dengan, memanggil, menyapa; mempraktikkan, membual, menyatakan, berkoar.\n
samudāciṇṇa: (pp dari **samudācarati**)  dipraktikkan, hanyut dalam.\n
samudāhara: nt. percakapan, pembicaraan, ucapan, ungkapan.\n
samudda: m.  samudra, lautan. [samudra ← Skt. samudra]
samuddharati: mengangkat, mengambil keluar dari, mengambil pergi, mengentaskan, menyelamatkan dari.\n
samupeta: a.  sepenuhnya dianugerahi dengan, memiliki, bersifat, tergolong.\n
samullapati: membicarakan, bercakap-cakap.\n
samūhanati: mengenyahkan, mencabut, menghapus, menghilangkan, membatalkan, meniadakan, mengakhiri.\n
sameti: berkumpul bersama, bertemu, bergabung dengan, bersatu, berpadu, mengetahui, mempertimbangkan, memikirkan; ger. **samecca** bergabung bersama, setelah dikuasai, dipelajari.\n
samodhāneti: menggabungkan, mengumpulkan, menghubungkan, mengaitkan.\n
sampakampati: bergetar, berguncang, menggegar, menggelatar, bergoyang.\n
sampajañña: nt.  pemahaman jernih; (Menurut DA. 1:183 ada empat jenis : _sātthaka_, _sappāya_, _gocara_, dan _asammoha_).\n
sampajāna: a.  pemahaman nan jelas, jernih memahami (_sata-sampajāna_  dengan penuh sati dan pemahaman); tahu betul, dengan penuh kesadaran, penuh pemahaman, dengan sengaja (_sampajāna-musāvāda_ berbohong dengan sengaja).\n
sampajjati: mencapai, berhasil, berjaya, sukses; menjadi, terjadi.\n
sampajjalita: a.  menyala, terbakar berkobar-kobar.\n
sampatta: (pp dari **sampāpuṇāti**)  tercapai, tiba, hadir, ditemui, dialami.\n
sampatti: f.  keberhasilan, sukses, capaian, hal mewujudkan, kebahagiaan, berkah, keberuntungan, kemujuran; keunggulan, kecemerlangan; keluhuran, kemuliaan, kemakmuran, kesejahteraan.\n
sampadā: f.  capaian (hasil yang dicapai), sukses, keberhasilan (prestasi), kebahagiaan, berkah, keberuntungan, kemujuran.\n
sampadāna: nt.  bentuk datif.\n
sampaduṭṭha: a. bersekongkol, berselingkuh, berbuat jahat.\n
sampanna: (pp dari **sampajjati**) berhasil, penuh dengan, dilengkapi dengan, dibekali dengan, dilingkupi; lengkap, sempurna, memiliki, berbekal, patut (_tayidaṁ bho gotama na sampannam evā ti_), cocok, lezat. [sempana ← Skt. sampanna]
sampayutta: m.  berasosiasi dengan, bersekutu dengan, bertautan dengan, berhubungan dengan, berkaitan dengan.\n
sampayoga: m.  persatuan, persekutuan.\n
samparāya: m.  keadaan mendatang, dunia berikut.\n
samparāyika: a.  berhubungan dengan dunia mendatang.\n
sampavāreti: membuat menerima, menawarkan, menyuguhi, melayani dengan.\n
sampavedhati: bergetar, berguncang, menggegar, menggelatar, bergoyang.\n
sampasādana: nt.  ketenangan, kedamaian, keheningan, kebeningan batin, kepercayaan diri.\n
sampahaṁsati: gembira, riang; kaus. **sampahaṁseti** menggembirakan, menyenangkan, menghibur, mendorong, membesarkan hati.\n
sampādeti: (kaus. dari **sampajjati**)  memperoleh, mendapat(kan), mampu menghasilkan (menelurkan); berupaya, berjuang, berupaya meraih.\n
sampāpuṇāti: mencapai, meraih, tiba di, bertemu dengan; kaus. **sampāpeti** membawa, membuat mencapai.\n
saṁpīḷeti: menekan, menggencet, mencemaskan, menindih, _menghimpit_.\n
sampha: a. nt.  tidak keruan; _samphaṁ bhāsati_ berbicara tidak keruan, omong kosong, bercakap angin; **~ppalāpa** pembicaraan yang tidak keruan, omong kosong.\n
samphassa: m.  kontak, sentuhan, reaksi.\n
sambahula: a.  banyak, beberapa, sejumlah.\n
sambāhati: menggosok, melangir (mencuci kepala), berkeramas.\n
sambodhi: f.  pencerahan (batin); kebijaksanaan tertinggi.\n
sambhajati: berkawan dengan, bergaul dengan, mencintai, melekat pada, lengket pada, sayang pada, setia akan.\n
sambhata: m.  hal mengumpulkan, menyimpan; nt. simpanan, perbekalan, perlengkapan.\n
sambhatta: (pp dari **sambhajati**) sayang, setia, teman.\n
sambhavati (sambhuṇāti, sambhoti): dihasilkan, muncul, timbul, pantas, cocok, kompeten, layak, hadir, menyaksikan, berada bersama-sama, mampu.\n
sambhāra: m.  timbunan, produk, persiapan, bekal, pelengkap, perangkat; bahan, material, bahan baku; unsur, elemen, komponen, faktor pokok; penghimpunan.\n
sambhāveti: (kaus. dari **sambhavati**)  melakukan, mengusahakan, mencapai, (melakukan) dengan sepenuh hati, meraih, menghasilkan, menelurkan, mempertim-bangkan (menganggap), menghormati, menghargai.\n
sambhāsā: f.  percakapan, perbincangan, pembicaraan.\n
sambhindati: mencampurkan.\n
sambhinna: (pp dari **sambhindati**) tercampur; (wanita) yang jenis kelaminnya tidak jelas, (wanita) yang berlubang campur (anus dan lubang kemaluan bercampur); terkuras, pecah.\n
sambhoga: makan, hidup bersama dengan, mengecap, menyantap, menikmati.\n
samma: 1. panggilan keakraban; 2. canang, gembreng; 3. (= **sammā**); **~kāra**a. secara benar.\n
sammajjati: menyapu, menggosok, mengusap.\n
sammajjana: nt.  hal menyapu.\n
sammaṭṭha: (pp dari **sammajjati**)  disapu, dibersihkan, tergosok, mulus.\n
sammata: (pp dari **sammannati**)  dianggap sebagai; dihormati; disetujui, disahkan, dibenarkan.\n
sammaddati: menginjak-injak, merapah.\n
sammannati: menyetujui, membenarkan, mengiakan, menyungguhkan, mengizinkan, mengabulkan, mengesahkan, memilih; menghormati.\n
sammasati: menyentuh, menangkap, mencengkeram, mencerap, memahami, menguasai; merenungkan, bermeditasi atas.\n
sammasana: nt.  penangkapan, penggenggaman, penguasaan, pemahaman; **~cāra** m. lingkup atau ranah pemahaman.\n
sammā: secara pantas, benar, sesuai, menyeluruh, seutuhnya, betul, terbaik, sempurna; **~sambodhi**f. pencerahan sempurna; kebuddhaan tertinggi.\n
sammiñjati (sammiñjeti) :  menekuk, melipat.\n
sammiñjita: (pp dari **sammiñjati**)  menekuk.\n
sammukha: a.  berhadap-hadapan dengan, dalam kehadiran, hadir, di depan; **sammukhā** (abl.) berhadapan, sebelum, di depan; di depan persamuhan lengkap orang-orang yang memenuhi syarat.\n
sammuṭṭha: (pp dari **sammussati**) lengah, lalai, lupa, alpa, tidak ingat (= _na ssarati_).\n
sammuti: f.  persetujuan, izin; pilihan, utusan; penetapan (perbatasan/sempadan); pendapat umum, permufakatan yang secara umum diterima; opini, doktrin; definisi, penjernihan, pernyataan; ungkapan populer, kata atau nama belaka; tradisi.\n
sammussati: lupa, lengah.\n
sammūḷha: m.  terhanyut (tergila-gila), bingung.\n
sammodati: turut berbahagia, bersuka cita, saling menyalami, beruluk-salam, ramah menyalami.\n
sammodanīya: a.  menyenangkan, bersahabat, tulus, ramah, akur.\n
sayati: 1.  (= seti)  berbaring; 2. bersandar pada.\n
sayana: nt.  hal berbaring, tidur; ranjang, dipan, tempat tidur.\n
sayaṁ: diri sendiri; oleh diri sendiri; **sayambhū**m. Sang Pencipta, yang mewujud dengan sendirinya. [saya ← Skt. svayaṁ]
sara: 1. m. alang-alang _Saccharum sara_; 2. m. panah (yang terbuat dari alang-alang jenis tersebut); 3. a. berjalan, bergerak, mengikuti; cair, mengalir; 4. m. nt. danau; 5. a. mengenang, mengingat; \\uf086 m. suara, bunyi, intonasi, aksen, vokal, huruf hidup. [suara ← Skt. svara]
saraṇa: nt.  perlindungan, naungan, lindungan, pertolongan, bantuan. [sarana ← Skt. ṡaraṇa]
sarati: 1. berjalan, mengalir, lari, bergerak sepanjang;  kaus.  **sāreti**membuat berjalan, menggosok, mencampurkan; 2. ingat; kaus. **sāreti** mengingatkan; 3. menggilas.\n
sarikkhaka: a.  sesuai dengan, mirip, seperti. (=**sarikkha**)
sarīra: nt.  badan (jasmani); mayat, jasad; tulang; relik. [sarira ← Skt. ṡarīra]
sarūpa: a.  yang berwujud sama, serupa; memiliki badan (wujud); **sarūpato** dari sisi dirinya sendiri (from their own side). [serupa ← Skt. sarūpa]
salākahattha: m.  tebak gambar telapak.\n
salākā: f.  panah; batangan kecil; pasak; bilah atau helai rumput; kupon atau kartu suara undi; bingkai payung; sejenis jarum; penis; batang kayu pipih kecil yang digunakan dalam pemungutan suara atau pembagian makanan; **~vutti**f.  hidup bersandar pada tiket makanan atau hidup bersandar pada helaian rumput (undian kupon makanan).\n
salila: nt. (aliran) air.\n
salla: nt.  anak panah, tusukan, cocok, sunduk, pacak.\n
sallakkheti: mengamati, memeriksa, mencermati; mencamkan; memahami; menyadari, menyimpulkan, merenungkan, mempertimbangkan; kaus. **sallakkhāpeti** membuat diperhatikan, membujuk, membuat mempertimbangkan.\n
sallīna: a.  lamban, ciut-menyusut.\n
sallekha: m.  penghapusan, penyingkiran atau pengenyahan (kotoran batin).\n
sasa: m.  kelinci.\n
sasī: m.  bulan.\n
sasura: m.  ayah mertua.\n
sassa: nt. padi-padian; panen; **~kamma** nt. cocok tanam; **~kāla** m. waktu panen, saat panen.\n
sassata: a.  langgeng, kekal, abadi; **~vada** m. (penganut) paham keabadian; eternalis, eternalisme.\n
sassū (sassu): f.  ibu mertua.\n
saha: bersama, dengan; **~dhammika** a. rekan sesama Dhamma, yang sesuai dengan Dhamma, seturut Dhamma.\n
sahattha: m.  dengan tangan sendiri.\n
sahavya: nt.  hal menjadi sahabat atau sekutu. [sahabat ← Skt. sāhāyya]
sahavyatā: f.  hal menjadi sahabat atau sekutu; ditengah-tengah.\n
sahasā: adv.  cepat-cepat, terburu-buru, tiba-tiba; tanpa berpikir panjang.\n
sahassa: nt. seribu.\n
sahāya: m.  kawan, rekan, teman, sobat. [sahaya ← Skt. sahāya]
sahāyaka: a.  kawan, teman, sekutu.\n
sāka: nt.  1. sayur-sayuran, tanaman pot, tanaman herba; 2. pohon jati (_Tectona grandis_).\n
sākaccheti: membicarakan, membahas, mendiskusikan.\n
sākuṇika: m.  penangkap burung.\n
sākyamuni: m.  orang suci dari suku Sakya, Buddha Gotama.\n
sākhā: f.  ranting, cabang; **~bhaṅga** seikat kayu bakar.\n
sāgara: m.  lautan, samudra, segara. [segara ← Skt. sāgara]
sājīva: nt.  tata hidup; jalan hidup; tata aturan yang mengatur tata kehidupan para bhikkhu; **~samāpanna** yang telah bergabung dalam jalan hidup.\n
sāṭaka: m.  pakaian luar, jubah, kain; pelapis, lamina, kulit, jangat.\n
sāṇī: f.  kain rami; sekat, tabir, tirai, tenda; **sāṇipasibbaka** kantung kain rami.\n
sāta: a.  menyenangkan; nt. kesenangan, kegembiraan, enak.\n
sāttha: a.  berguna, bermanfaat; bermakna.\n
sādiyati: menikmati, menyetujui, membiarkan, membolehkan, berkenan, bersedia.\n
sādhāraṇa: a.  umum, bersama.\n
sādhita: (pp dari **sādheti**)  telah dirampungkan, diselesaikan, dijalankan, disiapkan.\n
sādhiya: a.  yang dapat dirampungkan, dibereskan, diselesaikan.\n
sādhu: a.  baik, bagus, bajik, bermanfaat, saleh, berguna, silahkan.\n
sādhukāra: m.  hal menyoraki, hal mengucapkan _sādhu_ tanda setuju atau mendukung.\n
sādheti: menyelesaikan, merampungkan, membuat tumbuh berkembang, menyiapkan, melakukan, melaksanakan, mengadakan, menjalankan, mengakibatkan, memperjelas, menyimpulkan, membuktikan, membereskan utang, menarik kembali uang,
sāpateyya: nt.  harta kekayaan.\n
sāma: 1. m. hitam, gelap; kuning, keemasan, indah; 2. nt.  nyanyian, kidung (suci), kebaktian.\n
sāmaṁ: sendiri, diri sendiri.\n
sāmaggī: f.  lengkap, paripurna, bersatu-padu, manunggal.\n
sāmañña: 1. nt. yang umum, yang awam, yang sama, kesamaan, sebutan umum, kebersamaan, kesatuan, persesuaian, garis besar; 2. a.  sesuai dengan kepetapaan sejati; berupaya menjadi seorang samana atau petapa;  nt. kesamanaan, kepetapaan, status atau kehidupan kepetapaan.\n
sāmaṇera: m.  samanera, calon bhikkhu.\n
sāmaṇerī: f.  seorang calon bhikkhuni yang belum cukup umur untuk diupasampada menjadi bhikkhuni.\n
sāmanta: a.  bersebelahan, berdekatan, setara, bersambungan.\n
sāmāka: m.  sejenis padi-padian, _Panicum frumentaceum_.\n
sāmika: m.  pemilik; suami, wali; yang empunya, sponsor.\n
sāmin: m.  pemilik, penguasa, tuan; wali; suami. [suami ← Skt.svāmin]
sāmīci: f.  sesuai, pantas, patut, **~kamma** perbuatan yang pantas yakni penghormatan.\n
sāya: m.  senja atau malam; adv. **sāyaṁ** pada malam hari.\n
sāyaṇha: m.  sore hari; petang (pk 3-5).\n
sāyati: mencicipi, mengecap, makan.\n
sāyaniya: m.  cicipan, rasa; makanan lezat, enak, sedap.\n
sāra: a.  yang esensial (perlu sekali, mendasar, hakiki); yang terbaik, yang terunggul, kuat; m. yang terdalam, bagian yang terkeras dari sesuatu, inti batang pohon; kayu jenis terbaik; substansi, intisari, bagian terpilih (_sāre patiṭṭhito_ tegak di atas atau berlandaskan yang paling esensial); nilai. [sari ← Skt. sāra/sārin]
sārajjati: terpikat pada, tergila-gila pada.\n
sāratta: (pp dari **sārajjati**)  bersemangat berapi-api, dengan penuh nafsu, terpikat pada, tergila-gila pada.\n
sārathi (sārathī) :  m.  penjinak hewan.\n
sāraddha: a.  menggebu-gebu, meluap-luap, meledak-ledak, ganas, galak, rusuh. (_asāraddha = passaddhattā, vigatadaratho  _tenang, bebas dari kegelisahan)
sārāṇīya: a.  yang pantas diingat-ingat atau dikenang; sopan, bersahabat, menyenangkan.\n
sāri: m.  buah catur.\n
sāla: m. pohon Sal (?) (_Shorea robusta_); seraya atau pohon meranti (_Shorea leprosula_).\n
sālā: f.  aula, ruang yang besar, rumah, balai, gedung; bangsal, kandang.\n
sāli: m.  beras (jenis padi gogo, padi ladang, padi huma).\n
sālohita: m.  sanak famili, kerabat.\n
sāvaka: m.  penyimak, murid, siswa; **~saṅgha** meliputi _bhikkhusaṅgha_ dan _saṅgha_ dewa dan umat awam (siswa Sang Buddha); mencakup pula _Ariyasaṅgha_.\n
sāvajja: a.  tercela, salah; nt. cela, dosa, kesalahan.\n
sāvatthī :  f. nama ibu kota kerajaan Kosala (salah satu rajanya adalah Raja Pasenadi).\n
sāveti: (kaus. dari **suṇāti**) memperdengarkan, memberitahu, menyatakan, mengumumkan, menyebutkan.\n
sāsana: nt.  wejangan, ajaran, petuah, petunjuk, pesan, pengarahan. [sasana ← Skt. ṡāsana]
sāsapa: m.  biji moster (mostar).\n
sāhatthika: a.  dengan tangan sendiri.\n
siṁsapā: f.  pohon _Dalbergia sisu_ (pohon yang kuat dan besar).\n
sikkhati: belajar, berlatih, melatih.\n
sikkhamānā: f.  seorang wanita yang sedang menjalani masa percobaan sebelum ditahbiskan menjadi seorang bhikkhuni.\n
sikharaṇī: f.  wanita cacat kelamin.\n
sikkhā: f.  latihan, pelajaran; **~pada**nt. peraturan latihan, pokok latihan.\n
sikhā: f.  titik, ujung, puncak; nyala api.\n
sigāla (siṅgāla): m.  jakal (_Canis aureus_); serigala. [serigala ← Skt. sṛgāla]
sijjhati: berhasil, beres, berfaedah, cocok.\n
siñcati: memerciki, menyirami, mengeluarkan air (dari dalam perahu); pass. **siccati**.\n
sita: 1. a. tajam; 2. (pp dari **sayati**) tertusuk; bersandar pada, melekat pada; 3. (pp dari **sinoti**) terikat, terpikat; 4. a. putih; 5. nt. senyum.\n
sithila: a.  longgar, relaks, santai (melonggar), leluasa, tunduk, taat.\n
siddha: 1.  a.  telah dimasak;  2. (pp dari **sijjhati**) telah berakhir, berhasil, selesai; m. sejenis resi yang memiliki kekuatan gaib.\n
sineha (sneha): m.  cairan kental, cairan yang lengket-lengket, air atau getah tumbuh-tumbuhan; lemak; cinta, kasih, nafsu, keinginan.\n
sippa: nt.  seni, cabang ilmu pengetahuan, keterampilan atau kepandaian.\n
sippālaya: m. nt.  universitas, perguruan tinggi.\n
sibbati: menjahit, menjerumat, menisik.\n
sira: nt. m.  kepala.\n
silā: f.  batu, batu karang.\n
sīgha: a.  cepat; **sīghaṁ**adv.  dengan cepat.\n
sīta: a. nt.  dingin, sejuk.\n
sītala: a.  dingin, sejuk, tenang; nt. kedinginan; **sītalībhāva**menjadi dingin.\n
sīmā: f.  batasan, sima.\n
sīla: nt.  sifat, tabiat, perangai, watak, perilaku, tingkah laku; budi pekerti, akhlak, moralitas, tabiat baik, perangai baik. [sila ← ṡīla]
sīlana: tenang, mantap.\n
sīlavant: a.  bajik, bermoral, mematuhi sila, berakhlak baik, bersusila.\n
sīliya: nt.  perilaku, tindak-tanduk, karakter, tabiat.\n
sīvathikā: f.  pekuburan, pemakaman; tempat pembuangan mayat.\n
sīsa: nt.  timah; kepala, puncak, bagian tertinggi, depan, judul; titik (bagian) utama; bulir (padi), tongkol (jagung); **~ābhitāpa** kelengar matahari, sakit kepala.\n
sīha: m.  singa. [singa ← Skt. siṁha]
sīhī: f.  singa betina.\n
sukara: a.  mudah.\n
sukka: 1. m.  planet, bintang; nt. (air) mani, sperma; **~vāra** m. Hari Jumat; 2. a. putih, cemerlang, terang, murni, bagus; **~pakkha** m. paruh terang, suklapaksa.\n
sukkhati: mengering.\n
sukha: nt.  kebahagiaan, kenyamanan, nyenyak, perasaan bahagia, kebahagiaan jasmaniah. [suka ← Skt. sukha]
sukhallika: mengumbar nafsu.\n
sukhita: (pp dari **sukheti**)  bahagia, sejahtera, senang.\n
sukheti: membuat bahagia, membahagiakan.\n
sukhedhita: a.  = **sukha** **ṭhita** bahagia.\n
sugata:  ( = **sugatiṁ** **gata**) a.  dalam kondisi atau alam yang bahagia/ menyenangkan; yang beruntung, penuh berkah; yang telah mencapai alam bahagia, yang telah sukses bertempuh.\n
sugati: f. alam bahagia.\n
suṅka: m. nt.  bea, pajak, cukai; laba, keuntungan.\n
suṅkaghāta: m.  pos cukai, tempat penarikan cukai.\n
sucara: a.  mudah, gampang.\n
sucarita: nt.  perilaku benar/baik.\n
sujati: menyakitkan.\n
suñña: a.  kosong, tak berpenghuni, hampa, bukan sesuatu yang substansial, fenomenal; **~āgāra**m.  tempat kosong, lokasi tak berpenghuni, tempat yang sunyi atau sepi.\n
suññata: a.  kosong; hampa; tanpa nafsu, niat jahat dan kamma, terutama jiwa atau ego.\n
suṭṭhu: baik.\n
suṭṭhutā: f.  kebaikan, keunggulan.\n
suṇāti: (**suṇoti**) mendengar(kan), menyimak; **sūyati**, **suyyati**.\n
suṇisā: f.  menantu perempuan.\n
suṇhā: f.  menantu (perempuan).\n
sutta: 1. (pp dari **supati**) tertidur; nt. tidur; 2. nt. benang, tali, untai; sutta, wejangan (ajaran-ajaran yang dikumpulkan dalam sutta-pitaka); salah satu ragam kitab suci (▶ **navaṅga-buddhasāsana**); peraturan (dari _pāṭimokkha_); bab, bagian, nas, wejangan; syair purba, kutipan; kitab peraturan, buku nas, buku pegangan. [sutra ← Skt. sūtra]
suttaka: nt.  benang, untaian manik-manik atau permata.\n
suttantika: a.  yang mahir atau terpelajar atau pakar dalam hal Suttanta.\n
sudda: m.  orang yang berkasta sudra. [sudra ← Skt. ṡūdra]
suddha: (pp dari **sujjhati**) bersih, murni, bening; sederhana, belaka, semata-mata, takcampur.\n
suddhika: a.  yang berhubungan dengan kesucian, suci, murni, polos, sahaja, sederhana, ortodoks, tertata rapi, bergaris tepi (berpembatas).\n
sudhā: f.  makanan para dewa, (air) amerta; kapur (_lime_), semen, plester dinding, pemutihan.\n
sunakha: m.  anjing.\n
sundara: a.  indah, bagus, baik.\n
supati (suppati, soppati): tidur.\n
supina: m. nt.  mimpi; **~anta**m. mimpi; **supinantena** sedang dalam mimpi.\n
subha: a.  cemerlang, elok, penuh berkah, beralamat baik, menyenangkan, menarik (hati), baik;  nt. kesejahteraan, kebaikan, hal menyenangkan, kebersihan, keelokan, kesenangan.\n
subhaga: a.  beruntung, cantik, penuh pesona.\n
sumutta: a.  terbebas dengan baik, betul-betul lepas (dari).\n
sumbhaka: a.  yang tercampak, yang terjatuh, retak, peot.\n
suyyati: pass. dari **suṇāti**.\n
sura: m.  dewa.\n
surā: f.  minuman hasil fermentasi; a. gagah berani; m. pahlawan, matahari.\n
suriya: m.  surya, matahari. [surya ← Skt. sūrya]
sulasī: f.  kemangi, lampes, ruku-ruku (_Ocimum sanctum_); selasih, selasih jantan (?), selasih hitam (?) (_Ocimum basillicum_). [selasih ← Skt. surasī]
suvaṇṇa: a.  berwarna bagus, indah, bagus, menawan hati;  nt. emas, emas lantakan.\n
suve: ☞  **sve**
susāna: nt.  pekuburan, pemakaman; tempat peletakan mayat sampai membusuk.\n
susikkhita: a.  yang telah belajar dengan baik, terlatih baik; telah menguasai penuh, mudah dilatih, jinak, patuh.\n
susira: a.  berongga, bergerowong.\n
susu: 1. m. bocah, anak laki-laki; 2. suara “susu; suara mendesis; 3. nama sejenis hewan air.\n
sussati: mengering, melayu, menjadi haus, memudar, layu hati.\n
sūkara: m.  babi.\n
sūkarika: m.  penjagal babi.\n
sūcaka: m.  pengadu, pemfitnah, pegunjing, orang berlidah dua, pengadu domba.\n
sūci: f.  jarum; tusuk konde, pasak sanggul; gerendel pintu; pin, jarum penyemat, peniti, pasak; palang.\n
sūnā: f.  pejagalan, penjagalan, rumah jagal; **sūnaghara** rumah jagal.\n
sūpa: m.  sup, kari.\n
sūra: 1. a.  gagah berani;  m.  pahlawan, orang yang gagah berani; 2. m.  matahari.\n
sekha: (**sekkha**) m.  yang sedang berlatih, yang masih perlu berlatih, tak sempurna; yang masih harus belajar, yang belum mencapai kearahatan.\n
seṭṭha: a.  yang terkemuka, unggul, terbaik.\n
seṭṭhi: m.  kepala serikat sekerja, bendaharawan, bankir, saudagar kaya, saudagar besar.\n
seta: a. putih, murni.\n
setaṭṭhika: m.  bertulang belulang, dilanda bencana kelaparan;  f. jamur, lumut.\n
setu: m.  jembatan; jalan lintasan yang ditinggikan melewati rawa-rawa dsb; **~ghāta**a.  meruntuhkan jembatan (yang menghubungkan suatu tempat).\n
sedeti: (kaus. dari **sijjhati**)  membuat berpeluh, menghangatkan, menguapi.\n
senā: f.  pasukan, (bala) tentara, laskar (yang terdiri dari _hatthī_, _assā_, _rathā_, _pattī_).\n
senāsana: nt. tempat berbaring dan duduk, tempat pernaungan di mana seseorang dapat duduk dan berbaring, tempat pembaringan, tempat tinggal, kediaman, peristirahatan; perlengkapan peristirahatan; **~cārika**a.  berkelana dari satu peristirahatan ke peristirahatan lainnya.\n
seyya: a.  lebih baik, lebih bagus.\n
seyyathā: adv. seperti, sebagaimana, bagaikan **~pi** sama seperti, sebagaimana, bagaikan; **seyyathīdaṁ**sebagai berikut, yakni.\n
seyyā: f.  tempat tidur, ranjang, katil, pembaringan, peraduan; dipan; kasur, tilam, bantal, karpet, seprei, tikar, pelapik lantai, penutup lantai, jangat hewan, kain duduk, lapik duduk, kain penutup; hal berbaring, tidur.\n
sela: a.  berbatu-batu; m. batu, karang, kristal.\n
sevati: melayani, bergaul dengan, mengambil jalan, berpaling kepada, mempraktikkan, memeluk, menggunakan.\n
sevanā: f.  hal mengikuti, bergaul dengan, hidup bersama; hal meladeni.\n
sevāla: m.  tanaman lumut _Blyxa actandra_; rumput air.\n
sesa(ka): m.  sisa. [sisa ← Skt. ṡeṣa]
soka: m.  kesedihan, kepiluan.\n
sogata: m.  pengikut Sang Sugata, pengikut Buddha, umat Buddha.\n
socati: berdukacita atas, belasungkawa atas, berkabung atas, bersedih hati atas
soceyya: nt.  kemurnian.\n
soṇḍika: m.  penyuling dan penjual minuman keras; pemabuk.\n
soṇḍikā: f.  sulur tanaman menjalar; daging berlada; telaga.\n
sota: 1. nt. telinga, indra pendengaran; 2. m. nt.  arus, air bah, aliran air yang deras.\n
sotāpanna: m.  orang yang telah masuk arus, orang yang telah mencapai tingkat kesucian pertama.\n
sotti: f.  penggosok badan (perlengkapan mandi).\n
sotthi: f.  baik, aman, sejahtera, selamat (_Sotthi bhadante hotu rañño, sotthi janapadassāti_).\n
sodheti: (kaus. dari **sujjhati**)  membersihkan, memurnikan, memeriksa, mencari, memperbaiki, menyingkirkan, memutihkan (utang).\n
sobbha: m.  lubang, ceruk nan dalam.\n
sobhati: bersinar, bercahaya, tampak elok, bagus, cemerlang; kaus. sobheti membuat gemerlapan, memperindah, menyemarakkan.\n
somanassa: nt.  kegembiraan, kesukacitaan, kebahagiaan, kenyamanan batin.\n
sorivāra: m.  Hari Sabtu.\n
svākkhāta: a.  telah dibabarkan dengan baik; telah sempurna dipaparkan.\n
svāgata: m.  sambutan, selamat datang.\n
svātana: berkaitan dengan esok; **svātanāya**untuk hari berikutnya.\n
sve: adv.  besok, keesokan harinya.\n
ha: (kata penegas) hei, hallo, oh;  _iti ha_ begitulah; _itihītihaṁ_ begitu dan begitu; _heva  _yakni.\n
haṁsati: meremang, merinding, menggidikkan bulu roma, tegak bulu badan, bulu romanya berdiri.\n
haṭṭha: (pp dari **haṁsati**)  meremang, merinding, berdiri bulu romanya; gembira, bersuka cita, bahagia, girang.\n
hattha: m.  tangan; lengan bawah; ukuran satu hasta (Menurut Bhikkhu Thanissaro, 1 hasta = 24 **aṅgula**; 1 **sugatahattha** = 50 cm); **~pāsa**m. seperentangan tangan, jangkauan tangan. [hasta ← Skt. hasta]
hatthin: m.  gajah.\n
hadaya: m.  hati, batin; **~ṁgama**berkenan di hati; **~vatthu** nt. landasan hati, landasan batin.\n
hanati: menghantam, memukul, menggebuk, menghajar, mendera, menebah, mengirik; membunuh, menghancurkan, membinasakan, menyingkirkan; berak; pass. **haññati**.\n
handa: baiklah, sekarang, okei, marilah, aduh; sini; (_handāhaṁ_  baiklah, saya …).\n
haraṇaka: nt.  barang-barang yang bisa diangkut, barang-barang yang dapat dipindah-pindahkan, yang sedang dibawa, yang sedang dalam perjalanan.\n
harati: membawa, membawa serta; mengambil, mengumpulkan, menawarkan, menyingkirkan, membawa pergi, merampas, mencuri, menghancurkan, membinasakan.\n
harāpeti: menyebabkan dibawa, menawarkan.\n
harāyati: merasa malu, merasa _tertekan_ atau jengkel, dongkol, cemas.\n
harita: a. hijau, hijau pucat, kekuning-kuningan; segar (_haritena gomayena paṭhaviṁ opuñjāpetvā_); nt. sayuran, hijauan, tanaman; **haritā** f. emas.\n
halāhala: m. 1. sejenis racun yang mematikan; 2. kegaduhan, kerusuhan, kekacauan.\n
hasati (hassati): tertawa, bergembira; meringkik; kaus.  **hāseti** membuat tertawa, menggembirakan, menyenangkan.\n
hasita: (pp dari **hasati**) tertawa; bergembira;  nt.  tawa, kegembiraan.\n
hāpeti: 1. mengabaikan, menanggalkan, menghilangkan; menunda; mengurangi; mengalahkan; hilang; 2. mempersembahkan, menyembah, memupuk, memelihara.\n
hāyati: (pass. dari **jahati**) ditinggalkan, berkurang, mengecil, lenyap, menghilang.\n
hāraka: a.  membawa, mengambil, memperoleh, memindahkan; m. pembawa, pengambil.\n
hāriya: a.  membawa.\n
hi: sebab, karena, sungguh (_tañ hi tassa  _ia sungguh), tentu saja, memang; lah; **tena hi**baiklah kalau begitu, karena itu.\n
hita: a.  bermanfaat; m. sahabat, penolong; nt. manfaat, kemaslahatan.\n
hitesin: mengharapkan kesejahteraan pihak lain.\n
hiyyo: adv.  kemarin.\n
hirañña: nt.  emas, emas kepingan.\n
hiri (hirī): f.  rasa malu, keseganan. (Vism 464 _kāyaduccaritādīhi hiriyatī ti hiri; lajjāyetaṁ adhivacanaṁ._)
hīna: (pp dari **jahati**) _rendah_, nista, hina-dina, terkutuk, inferior; kekurangan. [hina ← Skt. hīna]
hīnāyāvatta: m.  orang yang kembali ke kehidupan duniawi, orang yang kembali ke kehidupan rendah.\n
hīyo: ☞  **hiyyo**
heṭṭhā: di bawah.\n
heṭṭhimā: a. terendah, lebih rendah; (tingkat) dasariah; **~tala** lapisan terbawah.\n
hetu: m.  “akar penyebab”, alasan, _sebab_, kondisi; demi.\n
heraññika: m.  tukang emas, pakar emas, pandai emas, penukar mata uang; **~phalaka**m. nt. bilah/papan/meja sang penukar mata uang.\n
hemanta: m.  musim dingin.\n
"""
