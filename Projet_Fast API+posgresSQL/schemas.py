from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

# Serializer for each class
class EtablissementInfo(BaseModel):  #serializer
    id: int
    siren: int
    nic: int
    siret: str
    statutDiffusionEtablissement: str
    dateCreationEtablissement: str
    trancheEffectifsEtablissement: str
    anneeEffectifsEtablissement: str
    activitePrincipaleRegistreMetiersEtablissement: str
    dateDernierTraitementEtablissement: str
    etablissementSiege: bool
    nombrePeriodesEtablissement: int

    class Config:
        orm_mode = True
        from_attributes = True

class AdressePrincipale(BaseModel):  #serializer
    siret: str
    complementAdresseEtablissement: str
    numeroVoieEtablissement: str
    indiceRepetitionEtablissement: str
    typeVoieEtablissement: str
    libelleVoieEtablissement: str
    codePostalEtablissement: str
    libelleCommuneEtablissement: str
    libelleCommuneEtrangerEtablissement: str
    distributionSpecialeEtablissement: str
    codeCommuneEtablissement: str
    codeCedexEtablissement: str
    libelleCedexEtablissement: str
    codePaysEtrangerEtablissement: str
    libellePaysEtrangerEtablissement: str

    class Config:
        orm_mode = True

class AdresseSecondaire(BaseModel):  #serializer
    siret: str
    complementAdresse2Etablissement: str
    numeroVoie2Etablissement: str
    indiceRepetition2Etablissement: str
    typeVoie2Etablissement: str
    libelleVoie2Etablissement: str
    codePostal2Etablissement: str
    libelleCommune2Etablissement: str
    libelleCommuneEtranger2Etablissement: str
    distributionSpeciale2Etablissement: str
    codeCommune2Etablissement: str
    codeCedex2Etablissement: str
    libelleCedex2Etablissement: str
    codePaysEtranger2Etablissement: str
    libellePaysEtranger2Etablissement: str

    class Config:
        orm_mode = True

class InfoSupplementaire(BaseModel):  #serializer
    siret: str
    dateDebut: str
    etatAdministratifEtablissement: str
    enseigne1Etablissement: str
    enseigne2Etablissement: str
    enseigne3Etablissement: str
    denominationUsuelleEtablissement: str
    activitePrincipaleEtablissement: str
    nomenclatureActivitePrincipaleEtablissement: str
    caractereEmployeurEtablissement: bool

    class Config:
        orm_mode = True