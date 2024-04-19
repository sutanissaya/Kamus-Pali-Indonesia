import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello.utils import show_code
import altair as alt
import numpy as np
import pandas as pd

LOGGER = get_logger(__name__)

st.set_page_config(page_title="Dictionary Test", page_icon="🌴")

"""
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
suve: ☞  **sve</b>
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
hīyo: ☞  **hiyyo</b>
heṭṭhā: di bawah.\n
heṭṭhimā: a. terendah, lebih rendah; (tingkat) dasariah; **~tala** lapisan terbawah.\n
hetu: m.  “akar penyebab”, alasan, _sebab_, kondisi; demi.\n
heraññika: m.  tukang emas, pakar emas, pandai emas, penukar mata uang; **~phalaka**m. nt. bilah/papan/meja sang penukar mata uang.\n
hemanta: m.  musim dingin.\n
"""
