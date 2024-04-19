import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")

"""
sara: "1. m. alang-alang <i>Saccharum sara</i>; 2. m. panah (yang terbuat dari alang-alang jenis tersebut); 3. a. berjalan, bergerak, mengikuti; cair, mengalir; 4. m. nt. danau; 5. a. mengenang, mengingat; \\uf086 m. suara, bunyi, intonasi, aksen, vokal, huruf hidup. [suara ← Skt. svara]"
saraṇa: "nt.  perlindungan, naungan, lindungan, pertolongan, bantuan. [sarana ← Skt. ṡaraṇa]"
sarati: "1. berjalan, mengalir, lari, bergerak sepanjang;  kaus.  <b>sāreti**membuat berjalan, menggosok, mencampurkan; 2. ingat; kaus. <b>sāreti** mengingatkan; 3. menggilas."\n
sarikkhaka: "a.  sesuai dengan, mirip, seperti. (=<b>sarikkha**)"
sarīra: "nt.  badan (jasmani); mayat, jasad; tulang; relik. [sarira ← Skt. ṡarīra]"
sarūpa: "a.  yang berwujud sama, serupa; memiliki badan (wujud); <b>sarūpato** dari sisi dirinya sendiri (from their own side). [serupa ← Skt. sarūpa]"
salākahattha: "m.  tebak gambar telapak."\n
salākā: "f.  panah; batangan kecil; pasak; bilah atau helai rumput; kupon atau kartu suara undi; bingkai payung; sejenis jarum; penis; batang kayu pipih kecil yang digunakan dalam pemungutan suara atau pembagian makanan; <b>~vutti**f.  hidup bersandar pada tiket makanan atau hidup bersandar pada helaian rumput (undian kupon makanan)."\n
salila: "nt. (aliran) air."\n
salla: "nt.  anak panah, tusukan, cocok, sunduk, pacak."\n
sallakkheti: "mengamati, memeriksa, mencermati; mencamkan; memahami; menyadari, menyimpulkan, merenungkan, mempertimbangkan; kaus. <b>sallakkhāpeti** membuat diperhatikan, membujuk, membuat mempertimbangkan."\n
sallīna: "a.  lamban, ciut-menyusut."\n
sallekha: "m.  penghapusan, penyingkiran atau pengenyahan (kotoran batin)."\n
sasa: "m.  kelinci."\n
sasī: "m.  bulan."\n
sasura: "m.  ayah mertua."\n
sassa: "nt. padi-padian; panen; <b>~kamma** nt. cocok tanam; <b>~kāla** m. waktu panen, saat panen."\n
sassata: "a.  langgeng, kekal, abadi; <b>~vada** m. (penganut) paham keabadian; eternalis, eternalisme."\n
sassū (sassu): "f.  ibu mertua."\n
saha: "bersama, dengan; <b>~dhammika** a. rekan sesama Dhamma, yang sesuai dengan Dhamma, seturut Dhamma."\n
sahattha: "m.  dengan tangan sendiri."\n
sahavya: "nt.  hal menjadi sahabat atau sekutu. [sahabat ← Skt. sāhāyya]"
sahavyatā: "f.  hal menjadi sahabat atau sekutu; ditengah-tengah."\n
sahasā: "adv.  cepat-cepat, terburu-buru, tiba-tiba; tanpa berpikir panjang."\n
sahassa: "nt. seribu."\n
sahāya: "m.  kawan, rekan, teman, sobat. [sahaya ← Skt. sahāya]"
sahāyaka: "a.  kawan, teman, sekutu."\n
sāka: "nt.  1. sayur-sayuran, tanaman pot, tanaman herba; 2. pohon jati (<i>Tectona grandis</i>)."\n
sākaccheti: "membicarakan, membahas, mendiskusikan."\n
sākuṇika: "m.  penangkap burung."\n
sākyamuni: "m.  orang suci dari suku Sakya, Buddha Gotama."\n
sākhā: "f.  ranting, cabang; <b>~bhaṅga** seikat kayu bakar."\n
sāgara: "m.  lautan, samudra, segara. [segara ← Skt. sāgara]"
sājīva: "nt.  tata hidup; jalan hidup; tata aturan yang mengatur tata kehidupan para bhikkhu; <b>~samāpanna** yang telah bergabung dalam jalan hidup."\n
sāṭaka: "m.  pakaian luar, jubah, kain; pelapis, lamina, kulit, jangat."\n
sāṇī: "f.  kain rami; sekat, tabir, tirai, tenda; <b>sāṇipasibbaka** kantung kain rami."\n
sāta: "a.  menyenangkan; nt. kesenangan, kegembiraan, enak."\n
sāttha: "a.  berguna, bermanfaat; bermakna."\n
sādiyati: "menikmati, menyetujui, membiarkan, membolehkan, berkenan, bersedia."\n
sādhāraṇa: "a.  umum, bersama."\n
sādhita: "(pp dari <b>sādheti**)  telah dirampungkan, diselesaikan, dijalankan, disiapkan."\n
sādhiya: "a.  yang dapat dirampungkan, dibereskan, diselesaikan."\n
sādhu: "a.  baik, bagus, bajik, bermanfaat, saleh, berguna, silahkan."\n
sādhukāra: "m.  hal menyoraki, hal mengucapkan <i>sādhu</i> tanda setuju atau mendukung."\n
sādheti: "menyelesaikan, merampungkan, membuat tumbuh berkembang, menyiapkan, melakukan, melaksanakan, mengadakan, menjalankan, mengakibatkan, memperjelas, menyimpulkan, membuktikan, membereskan utang, menarik kembali uang,"
sāpateyya: "nt.  harta kekayaan."\n
sāma: "1. m. hitam, gelap; kuning, keemasan, indah; 2. nt.  nyanyian, kidung (suci), kebaktian."\n
sāmaṁ: "sendiri, diri sendiri."\n
sāmaggī: "f.  lengkap, paripurna, bersatu-padu, manunggal."\n
sāmañña: "1. nt. yang umum, yang awam, yang sama, kesamaan, sebutan umum, kebersamaan, kesatuan, persesuaian, garis besar; 2. a.  sesuai dengan kepetapaan sejati; berupaya menjadi seorang samana atau petapa;  nt. kesamanaan, kepetapaan, status atau kehidupan kepetapaan."\n
sāmaṇera: "m.  samanera, calon bhikkhu."\n
sāmaṇerī: "f.  seorang calon bhikkhuni yang belum cukup umur untuk diupasampada menjadi bhikkhuni."\n
sāmanta: "a.  bersebelahan, berdekatan, setara, bersambungan."\n
sāmāka: "m.  sejenis padi-padian, <i>Panicum frumentaceum</i>."\n
sāmika: "m.  pemilik; suami, wali; yang empunya, sponsor."\n
sāmin: "m.  pemilik, penguasa, tuan; wali; suami. [suami ← Skt.svāmin]"
sāmīci: "f.  sesuai, pantas, patut, <b>~kamma** perbuatan yang pantas yakni penghormatan."\n
sāya: "m.  senja atau malam; adv. <b>sāyaṁ** pada malam hari."\n
sāyaṇha: "m.  sore hari; petang (pk 3-5)."\n
sāyati: "mencicipi, mengecap, makan."\n
sāyaniya: "m.  cicipan, rasa; makanan lezat, enak, sedap."\n
sāra: "a.  yang esensial (perlu sekali, mendasar, hakiki); yang terbaik, yang terunggul, kuat; m. yang terdalam, bagian yang terkeras dari sesuatu, inti batang pohon; kayu jenis terbaik; substansi, intisari, bagian terpilih (<i>sāre patiṭṭhito</i> tegak di atas atau berlandaskan yang paling esensial); nilai. [sari ← Skt. sāra/sārin]"
sārajjati: "terpikat pada, tergila-gila pada."\n
sāratta: "(pp dari <b>sārajjati**)  bersemangat berapi-api, dengan penuh nafsu, terpikat pada, tergila-gila pada."\n
sārathi (sārathī) : " m.  penjinak hewan."\n
sāraddha: "a.  menggebu-gebu, meluap-luap, meledak-ledak, ganas, galak, rusuh. (<i>asāraddha = passaddhattā, vigatadaratho  </i>tenang, bebas dari kegelisahan)"
sārāṇīya: "a.  yang pantas diingat-ingat atau dikenang; sopan, bersahabat, menyenangkan."\n
sāri: "m.  buah catur."\n
sāla: "m. pohon Sal (?) (<i>Shorea robusta</i>); seraya atau pohon meranti (<i>Shorea leprosula</i>)."\n
sālā: "f.  aula, ruang yang besar, rumah, balai, gedung; bangsal, kandang."\n
sāli: "m.  beras (jenis padi gogo, padi ladang, padi huma)."\n
sālohita: "m.  sanak famili, kerabat."\n
sāvaka: "m.  penyimak, murid, siswa; <b>~saṅgha** meliputi <i>bhikkhusaṅgha</i> dan <i>saṅgha</i> dewa dan umat awam (siswa Sang Buddha); mencakup pula <i>Ariyasaṅgha</i>."\n
sāvajja: "a.  tercela, salah; nt. cela, dosa, kesalahan."\n
sāvatthī : " f. nama ibu kota kerajaan Kosala (salah satu rajanya adalah Raja Pasenadi)."\n
sāveti: "(kaus. dari <b>suṇāti**) memperdengarkan, memberitahu, menyatakan, mengumumkan, menyebutkan."\n
sāsana: "nt.  wejangan, ajaran, petuah, petunjuk, pesan, pengarahan. [sasana ← Skt. ṡāsana]"
sāsapa: "m.  biji moster (mostar)."\n
sāhatthika: "a.  dengan tangan sendiri."\n
siṁsapā: "f.  pohon <i>Dalbergia sisu</i> (pohon yang kuat dan besar)."\n
sikkhati: "belajar, berlatih, melatih."\n
sikkhamānā: "f.  seorang wanita yang sedang menjalani masa percobaan sebelum ditahbiskan menjadi seorang bhikkhuni."\n
sikharaṇī: "f.  wanita cacat kelamin."\n
sikkhā: "f.  latihan, pelajaran; <b>~pada**nt. peraturan latihan, pokok latihan."\n
sikhā: "f.  titik, ujung, puncak; nyala api."\n
sigāla (siṅgāla): "m.  jakal (<i>Canis aureus</i>); serigala. [serigala ← Skt. sṛgāla]"
sijjhati: "berhasil, beres, berfaedah, cocok."\n
siñcati: "memerciki, menyirami, mengeluarkan air (dari dalam perahu); pass. <b>siccati**."\n
sita: "1. a. tajam; 2. (pp dari <b>sayati**) tertusuk; bersandar pada, melekat pada; 3. (pp dari <b>sinoti**) terikat, terpikat; 4. a. putih; 5. nt. senyum."\n
sithila: "a.  longgar, relaks, santai (melonggar), leluasa, tunduk, taat."\n
siddha: "1.  a.  telah dimasak;  2. (pp dari <b>sijjhati**) telah berakhir, berhasil, selesai; m. sejenis resi yang memiliki kekuatan gaib."\n
sineha (sneha): "m.  cairan kental, cairan yang lengket-lengket, air atau getah tumbuh-tumbuhan; lemak; cinta, kasih, nafsu, keinginan."\n
sippa: "nt.  seni, cabang ilmu pengetahuan, keterampilan atau kepandaian."\n
sippālaya: "m. nt.  universitas, perguruan tinggi."\n
sibbati: "menjahit, menjerumat, menisik."\n
sira: "nt. m.  kepala."\n
silā: "f.  batu, batu karang."\n
sīgha: "a.  cepat; <b>sīghaṁ**adv.  dengan cepat."\n
sīta: "a. nt.  dingin, sejuk."\n
sītala: "a.  dingin, sejuk, tenang; nt. kedinginan; <b>sītalībhāva**menjadi dingin."\n
sīmā: "f.  batasan, sima."\n
sīla: "nt.  sifat, tabiat, perangai, watak, perilaku, tingkah laku; budi pekerti, akhlak, moralitas, tabiat baik, perangai baik. [sila ← ṡīla]"
sīlana: "tenang, mantap."\n
sīlavant: "a.  bajik, bermoral, mematuhi sila, berakhlak baik, bersusila."\n
sīliya: "nt.  perilaku, tindak-tanduk, karakter, tabiat."\n
sīvathikā: "f.  pekuburan, pemakaman; tempat pembuangan mayat."\n
sīsa: "nt.  timah; kepala, puncak, bagian tertinggi, depan, judul; titik (bagian) utama; bulir (padi), tongkol (jagung); <b>~ābhitāpa** kelengar matahari, sakit kepala."\n
sīha: "m.  singa. [singa ← Skt. siṁha]"
sīhī: "f.  singa betina."\n
sukara: "a.  mudah."\n
sukka: "1. m.  planet, bintang; nt. (air) mani, sperma; <b>~vāra** m. Hari Jumat; 2. a. putih, cemerlang, terang, murni, bagus; <b>~pakkha** m. paruh terang, suklapaksa."\n
sukkhati: "mengering."\n
sukha: "nt.  kebahagiaan, kenyamanan, nyenyak, perasaan bahagia, kebahagiaan jasmaniah. [suka ← Skt. sukha]"
sukhallika: "mengumbar nafsu."\n
sukhita: "(pp dari <b>sukheti**)  bahagia, sejahtera, senang."\n
sukheti: "membuat bahagia, membahagiakan."\n
sukhedhita: "a.  = <b>sukha** <b>ṭhita** bahagia."\n
sugata: " ( = <b>sugatiṁ** <b>gata**) a.  dalam kondisi atau alam yang bahagia/ menyenangkan; yang beruntung, penuh berkah; yang telah mencapai alam bahagia, yang telah sukses bertempuh."\n
sugati: "f. alam bahagia."\n
suṅka: "m. nt.  bea, pajak, cukai; laba, keuntungan."\n
suṅkaghāta: "m.  pos cukai, tempat penarikan cukai."\n
sucara: "a.  mudah, gampang."\n
sucarita: "nt.  perilaku benar/baik."\n
sujati: "menyakitkan."\n
suñña: "a.  kosong, tak berpenghuni, hampa, bukan sesuatu yang substansial, fenomenal; <b>~āgāra**m.  tempat kosong, lokasi tak berpenghuni, tempat yang sunyi atau sepi."\n
suññata: "a.  kosong; hampa; tanpa nafsu, niat jahat dan kamma, terutama jiwa atau ego."\n
suṭṭhu: "baik."\n
suṭṭhutā: "f.  kebaikan, keunggulan."\n
suṇāti: "(<b>suṇoti**) mendengar(kan), menyimak; <b>sūyati**, <b>suyyati**."\n
suṇisā: "f.  menantu perempuan."\n
suṇhā: "f.  menantu (perempuan)."\n
sutta: "1. (pp dari <b>supati**) tertidur; nt. tidur; 2. nt. benang, tali, untai; sutta, wejangan (ajaran-ajaran yang dikumpulkan dalam sutta-pitaka); salah satu ragam kitab suci (▶ <b>navaṅga-buddhasāsana**); peraturan (dari <i>pāṭimokkha</i>); bab, bagian, nas, wejangan; syair purba, kutipan; kitab peraturan, buku nas, buku pegangan. [sutra ← Skt. sūtra]"
suttaka: "nt.  benang, untaian manik-manik atau permata."\n
suttantika: "a.  yang mahir atau terpelajar atau pakar dalam hal Suttanta."\n
sudda: "m.  orang yang berkasta sudra. [sudra ← Skt. ṡūdra]"
suddha: "(pp dari <b>sujjhati**) bersih, murni, bening; sederhana, belaka, semata-mata, takcampur."\n
suddhika: "a.  yang berhubungan dengan kesucian, suci, murni, polos, sahaja, sederhana, ortodoks, tertata rapi, bergaris tepi (berpembatas)."\n
sudhā: "f.  makanan para dewa, (air) amerta; kapur (<i>lime</i>), semen, plester dinding, pemutihan."\n
sunakha: "m.  anjing."\n
sundara: "a.  indah, bagus, baik."\n
supati (suppati, soppati): "tidur."\n
supina: "m. nt.  mimpi; <b>~anta**m. mimpi; <b>supinantena** sedang dalam mimpi."\n
subha: "a.  cemerlang, elok, penuh berkah, beralamat baik, menyenangkan, menarik (hati), baik;  nt. kesejahteraan, kebaikan, hal menyenangkan, kebersihan, keelokan, kesenangan."\n
subhaga: "a.  beruntung, cantik, penuh pesona."\n
sumutta: "a.  terbebas dengan baik, betul-betul lepas (dari)."\n
sumbhaka: "a.  yang tercampak, yang terjatuh, retak, peot."\n
suyyati: "pass. dari <b>suṇāti**."\n
sura: "m.  dewa."\n
surā: "f.  minuman hasil fermentasi; a. gagah berani; m. pahlawan, matahari."\n
suriya: "m.  surya, matahari. [surya ← Skt. sūrya]"
sulasī: "f.  kemangi, lampes, ruku-ruku (<i>Ocimum sanctum</i>); selasih, selasih jantan (?), selasih hitam (?) (<i>Ocimum basillicum</i>). [selasih ← Skt. surasī]"
suvaṇṇa: "a.  berwarna bagus, indah, bagus, menawan hati;  nt. emas, emas lantakan."\n
suve: "☞  <b>sve</b>"
susāna: "nt.  pekuburan, pemakaman; tempat peletakan mayat sampai membusuk."\n
susikkhita: "a.  yang telah belajar dengan baik, terlatih baik; telah menguasai penuh, mudah dilatih, jinak, patuh."\n
susira: "a.  berongga, bergerowong."\n
susu: "1. m. bocah, anak laki-laki; 2. suara “susu; suara mendesis; 3. nama sejenis hewan air."\n
sussati: "mengering, melayu, menjadi haus, memudar, layu hati."\n
sūkara: "m.  babi."\n
sūkarika: "m.  penjagal babi."\n
sūcaka: "m.  pengadu, pemfitnah, pegunjing, orang berlidah dua, pengadu domba."\n
sūci: "f.  jarum; tusuk konde, pasak sanggul; gerendel pintu; pin, jarum penyemat, peniti, pasak; palang."\n
sūnā: "f.  pejagalan, penjagalan, rumah jagal; <b>sūnaghara** rumah jagal."\n
sūpa: "m.  sup, kari."\n
sūra: "1. a.  gagah berani;  m.  pahlawan, orang yang gagah berani; 2. m.  matahari."\n
sekha: "(<b>sekkha**) m.  yang sedang berlatih, yang masih perlu berlatih, tak sempurna; yang masih harus belajar, yang belum mencapai kearahatan."\n
seṭṭha: "a.  yang terkemuka, unggul, terbaik."\n
seṭṭhi: "m.  kepala serikat sekerja, bendaharawan, bankir, saudagar kaya, saudagar besar."\n
seta: "a. putih, murni."\n
setaṭṭhika: "m.  bertulang belulang, dilanda bencana kelaparan;  f. jamur, lumut."\n
setu: "m.  jembatan; jalan lintasan yang ditinggikan melewati rawa-rawa dsb; <b>~ghāta**a.  meruntuhkan jembatan (yang menghubungkan suatu tempat)."\n
sedeti: "(kaus. dari <b>sijjhati**)  membuat berpeluh, menghangatkan, menguapi."\n
senā: "f.  pasukan, (bala) tentara, laskar (yang terdiri dari <i>hatthī</i>, <i>assā</i>, <i>rathā</i>, <i>pattī</i>)."\n
senāsana: "nt. tempat berbaring dan duduk, tempat pernaungan di mana seseorang dapat duduk dan berbaring, tempat pembaringan, tempat tinggal, kediaman, peristirahatan; perlengkapan peristirahatan; <b>~cārika**a.  berkelana dari satu peristirahatan ke peristirahatan lainnya."\n
seyya: "a.  lebih baik, lebih bagus."\n
seyyathā: "adv. seperti, sebagaimana, bagaikan <b>~pi** sama seperti, sebagaimana, bagaikan; <b>seyyathīdaṁ**sebagai berikut, yakni."\n
seyyā: "f.  tempat tidur, ranjang, katil, pembaringan, peraduan; dipan; kasur, tilam, bantal, karpet, seprei, tikar, pelapik lantai, penutup lantai, jangat hewan, kain duduk, lapik duduk, kain penutup; hal berbaring, tidur."\n
sela: "a.  berbatu-batu; m. batu, karang, kristal."\n
sevati: "melayani, bergaul dengan, mengambil jalan, berpaling kepada, mempraktikkan, memeluk, menggunakan."\n
sevanā: "f.  hal mengikuti, bergaul dengan, hidup bersama; hal meladeni."\n
sevāla: "m.  tanaman lumut <i>Blyxa actandra</i>; rumput air."\n
sesa(ka): "m.  sisa. [sisa ← Skt. ṡeṣa]"
soka: "m.  kesedihan, kepiluan."\n
sogata: "m.  pengikut Sang Sugata, pengikut Buddha, umat Buddha."\n
socati: "berdukacita atas, belasungkawa atas, berkabung atas, bersedih hati atas"
soceyya: "nt.  kemurnian."\n
soṇḍika: "m.  penyuling dan penjual minuman keras; pemabuk."\n
soṇḍikā: "f.  sulur tanaman menjalar; daging berlada; telaga."\n
sota: "1. nt. telinga, indra pendengaran; 2. m. nt.  arus, air bah, aliran air yang deras."\n
sotāpanna: "m.  orang yang telah masuk arus, orang yang telah mencapai tingkat kesucian pertama."\n
sotti: "f.  penggosok badan (perlengkapan mandi)."\n
sotthi: "f.  baik, aman, sejahtera, selamat (<i>Sotthi bhadante hotu rañño, sotthi janapadassāti</i>)."\n
sodheti: "(kaus. dari <b>sujjhati**)  membersihkan, memurnikan, memeriksa, mencari, memperbaiki, menyingkirkan, memutihkan (utang)."\n
sobbha: "m.  lubang, ceruk nan dalam."\n
sobhati: "bersinar, bercahaya, tampak elok, bagus, cemerlang; kaus. sobheti membuat gemerlapan, memperindah, menyemarakkan."\n
somanassa: "nt.  kegembiraan, kesukacitaan, kebahagiaan, kenyamanan batin."\n
sorivāra: "m.  Hari Sabtu."\n
svākkhāta: "a.  telah dibabarkan dengan baik; telah sempurna dipaparkan."\n
svāgata: "m.  sambutan, selamat datang."\n
svātana: "berkaitan dengan esok; <b>svātanāya**untuk hari berikutnya."\n
sve: "adv.  besok, keesokan harinya."\n
ha: "(kata penegas) hei, hallo, oh;  <i>iti ha</i> begitulah; <i>itihītihaṁ</i> begitu dan begitu; <i>heva  </i>yakni."\n
haṁsati: "meremang, merinding, menggidikkan bulu roma, tegak bulu badan, bulu romanya berdiri."\n
haṭṭha: "(pp dari <b>haṁsati**)  meremang, merinding, berdiri bulu romanya; gembira, bersuka cita, bahagia, girang."\n
hattha: "m.  tangan; lengan bawah; ukuran satu hasta (Menurut Bhikkhu Thanissaro, 1 hasta = 24 <b>aṅgula**; 1 <b>sugatahattha** = 50 cm); <b>~pāsa**m. seperentangan tangan, jangkauan tangan. [hasta ← Skt. hasta]"
hatthin: "m.  gajah."\n
hadaya: "m.  hati, batin; <b>~ṁgama**berkenan di hati; <b>~vatthu** nt. landasan hati, landasan batin."\n
hanati: "menghantam, memukul, menggebuk, menghajar, mendera, menebah, mengirik; membunuh, menghancurkan, membinasakan, menyingkirkan; berak; pass. <b>haññati**."\n
handa: "baiklah, sekarang, okei, marilah, aduh; sini; (<i>handāhaṁ</i>  baiklah, saya …)."\n
haraṇaka: "nt.  barang-barang yang bisa diangkut, barang-barang yang dapat dipindah-pindahkan, yang sedang dibawa, yang sedang dalam perjalanan."\n
harati: "membawa, membawa serta; mengambil, mengumpulkan, menawarkan, menyingkirkan, membawa pergi, merampas, mencuri, menghancurkan, membinasakan."\n
harāpeti: "menyebabkan dibawa, menawarkan."\n
harāyati: "merasa malu, merasa <i>tertekan</i> atau jengkel, dongkol, cemas."\n
harita: "a. hijau, hijau pucat, kekuning-kuningan; segar (<i>haritena gomayena paṭhaviṁ opuñjāpetvā</i>); nt. sayuran, hijauan, tanaman; <b>haritā** f. emas."\n
halāhala: "m. 1. sejenis racun yang mematikan; 2. kegaduhan, kerusuhan, kekacauan."\n
hasati (hassati): "tertawa, bergembira; meringkik; kaus.  <b>hāseti** membuat tertawa, menggembirakan, menyenangkan."\n
hasita: "(pp dari <b>hasati**) tertawa; bergembira;  nt.  tawa, kegembiraan."\n
hāpeti: "1. mengabaikan, menanggalkan, menghilangkan; menunda; mengurangi; mengalahkan; hilang; 2. mempersembahkan, menyembah, memupuk, memelihara."\n
hāyati: "(pass. dari <b>jahati**) ditinggalkan, berkurang, mengecil, lenyap, menghilang."\n
hāraka: "a.  membawa, mengambil, memperoleh, memindahkan; m. pembawa, pengambil."\n
hāriya: "a.  membawa."\n
hi: "sebab, karena, sungguh (<i>tañ hi tassa  </i>ia sungguh), tentu saja, memang; lah; <b>tena hi**baiklah kalau begitu, karena itu."\n
hita: "a.  bermanfaat; m. sahabat, penolong; nt. manfaat, kemaslahatan."\n
hitesin: "mengharapkan kesejahteraan pihak lain."\n
hiyyo: "adv.  kemarin."\n
hirañña: "nt.  emas, emas kepingan."\n
hiri (hirī): "f.  rasa malu, keseganan. (Vism 464 <i>kāyaduccaritādīhi hiriyatī ti hiri; lajjāyetaṁ adhivacanaṁ.</i>)"
hīna: "(pp dari <b>jahati**) <i>rendah</i>, nista, hina-dina, terkutuk, inferior; kekurangan. [hina ← Skt. hīna]"
hīnāyāvatta: "m.  orang yang kembali ke kehidupan duniawi, orang yang kembali ke kehidupan rendah."\n
hīyo: "☞  <b>hiyyo</b>"
heṭṭhā: "di bawah."\n
heṭṭhimā: "a. terendah, lebih rendah; (tingkat) dasariah; <b>~tala** lapisan terbawah."\n
hetu: "m.  “akar penyebab”, alasan, <i>sebab</i>, kondisi; demi."\n
heraññika: "m.  tukang emas, pakar emas, pandai emas, penukar mata uang; <b>~phalaka**m. nt. bilah/papan/meja sang penukar mata uang."\n
hemanta: "m.  musim dingin."\n
"""
