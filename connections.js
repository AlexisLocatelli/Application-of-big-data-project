const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/Enterprise');
const db = mongoose.connection;

db.on('error', console.error.bind(console, 'Erreur de connexion à la base de données :'));
db.once('open', async () => {
  console.log('Connexion réussie à la base de données');
});

const enterpriseSchema = new mongoose.Schema({
  siren : Number,
  nic : Number,
  siret : Number,
  statutDiffusionEtablissement : String,
  dateCreationEtablissement : Date,
  trancheEffectifsEtablissement : String,
  anneeEffectifsEtablissement : Number,
  activitePrincipaleRegistreMetiersEtablissement : String,
  dateDernierTraitementEtablissement : Date,
  etablissementSiege : Boolean,
  nombrePeriodesEtablissement : Number,
  complementAdresseEtablissement : String,
  numeroVoieEtablissement : String,
  indiceRepetitionEtablissement : String,
  typeVoieEtablissement : String,
  libelleVoieEtablissement : String,
  codePostalEtablissement : Number,
  libelleCommuneEtablissement : String,
  libelleCommuneEtrangerEtablissement : String,
  distributionSpecialeEtablissement : String,
  codeCommuneEtablissement : Number,
  codeCedexEtablissement : Number,
  libelleCedexEtablissement : String,
  codePaysEtrangerEtablissement : String,
  libellePaysEtrangerEtablissement : String,
  complementAdresse2Etablissement : String,
  numeroVoie2Etablissement : Number,
  indiceRepetition2Etablissement : String,
  typeVoie2Etablissement : String,
  libelleVoie2Etablissement : String,
  codePostal2Etablissement : Number,
  libelleCommune2Etablissement : String,
  libelleCommuneEtranger2Etablissement : String,
  distributionSpeciale2Etablissement : String,
  codeCommune2Etablissement : Number,
  codeCedex2Etablissement : String,
  libelleCedex2Etablissement : String,
  codePaysEtranger2Etablissement : String,
  libellePaysEtranger2Etablissement : String,
  dateDebut : Date,
  etatAdministratifEtablissement : String,
  enseigne1Etablissement : String,
  enseigne2Etablissement : String,
  enseigne3Etablissement : String,
  denominationUsuelleEtablissement : String,
  activitePrincipaleEtablissement : String,
  nomenclatureActivitePrincipaleEtablissement : String,
  caractereEmployeurEtablissement : String,
});
const Enterprise = mongoose.model('enterprises', enterpriseSchema);

module.exports = {
    Enterprise
}