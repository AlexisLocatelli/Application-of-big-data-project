const mongoose = require('mongoose');

// Connexion à la base de données MongoDB (assurez-vous d'avoir MongoDB installé localement)
mongoose.connect('mongodb+srv://alexisLocatelli:ArZnfglk7nhG2IHa@enterprisecluster.ism0vxp.mongodb.net/Enterprise');
const db = mongoose.connection;

// Gestion des erreurs de connexion à la base de données
db.on('error', console.error.bind(console, 'Erreur de connexion à la base de données :'));
db.once('open', () => {
  console.log('Connexion réussie à la base de données');
});

// Définir un schéma pour le modèle d'entreprise
const enterpriseSchema = new mongoose.Schema({
  siren : String,
  nic : String,
  siret : String,
  statutDiffusionEtablissement : String,
  dateCreationEtablissement : String,
  trancheEffectifsEtablissement : String,
  anneeEffectifsEtablissement : String,
  activitePrincipaleRegistreMetiersEtablissement : String,
  dateDernierTraitementEtablissement : String,
  etablissementSiege : String,
  nombrePeriodesEtablissement : String,
  complementAdresseEtablissement : String,
  numeroVoieEtablissement : String,
  indiceRepetitionEtablissement : String,
  typeVoieEtablissement : String,
  libelleVoieEtablissement : String,
  codePostalEtablissement : String,
  libelleCommuneEtablissement : String,
  libelleCommuneEtrangerEtablissement : String,
  distributionSpecialeEtablissement : String,
  codeCommuneEtablissement : String,
  codeCedexEtablissement : String,
  libelleCedexEtablissement : String,
  codePaysEtrangerEtablissement : String,
  libellePaysEtrangerEtablissement : String,
  complementAdresse2Etablissement : String,
  numeroVoie2Etablissement : String,
  indiceRepetition2Etablissement : String,
  typeVoie2Etablissement : String,
  libelleVoie2Etablissement : String,
  codePostal2Etablissement : String,
  libelleCommune2Etablissement : String,
  libelleCommuneEtranger2Etablissement : String,
  distributionSpeciale2Etablissement : String,
  codeCommune2Etablissement : String,
  codeCedex2Etablissement : String,
  libelleCedex2Etablissement : String,
  codePaysEtranger2Etablissement : String,
  libellePaysEtranger2Etablissement : String,
  dateDebut : String,
  etatAdministratifEtablissement : String,
  enseigne1Etablissement : String,
  enseigne2Etablissement : String,
  enseigne3Etablissement : String,
  denominationUsuelleEtablissement : String,
  activitePrincipaleEtablissement : String,
  nomenclatureActivitePrincipaleEtablissement : String,
  caractereEmployeurEtablissement : String,
});

// Créer un modèle d'entreprise à partir du schéma
const Enterprise = mongoose.model('enterprises', enterpriseSchema);

async function get_enterprise(siret) {
  const enterprise = await Enterprise.find({siret:siret}).exec();
  return enterprise
}

async function delete_enterprise(siret) {
  const enterprise = await Enterprise.find({siret:siret}).exec();
  enterprise.deleteone();
}

async function post_enterprise(enterprise) {
  const newEnterprise = new Enterprise(req.body);
  await newEnterprise.save();
}

module.exports = {
    get_enterprise,
    post_enterprise,
    delete_enterprise
}