from database import Base
from sqlalchemy import String, Boolean, Column, Text, Date, Integer, BigInteger, Float


class EtablissementInfo(Base):
    __tablename__ = 'etablissement_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    siren = Column(BigInteger)  # int64 dans votre CSV
    nic = Column(Integer)  # int64 dans votre CSV
    siret = Column(String)  # object dans votre CSV
    statutDiffusionEtablissement = Column(String)  # object dans votre CSV
    dateCreationEtablissement = Column(String)  # object dans votre CSV
    trancheEffectifsEtablissement = Column(String)  # object dans votre CSV
    anneeEffectifsEtablissement = Column(String)  # float64 dans votre CSV
    activitePrincipaleRegistreMetiersEtablissement = Column(String)  # object dans votre CSV
    dateDernierTraitementEtablissement = Column(String)  # object dans votre CSV
    etablissementSiege = Column(Boolean)  # bool dans votre CSV
    nombrePeriodesEtablissement = Column(Integer)

    def __repr__(self):
        return f"<EtablissementInfo id={self.siret}>"

'''class AdressePrincipale(Base):
    __tablename__ = "AdressePrincipale"
    id = Column(Integer, primary_key=True, autoincrement=True)
    siret = Column(String, primary_key=True)
    complementAdresseEtablissement=Column(String)
    numeroVoieEtablissement=Column(String)
    indiceRepetitionEtablissement=Column(String)
    typeVoieEtablissement=Column(String)
    libelleVoieEtablissement=Column(String)
    codePostalEtablissement=Column(String)
    libelleCommuneEtablissement=Column(String)
    libelleCommuneEtrangerEtablissement=Column(String)
    distributionSpecialeEtablissement=Column(String)
    codeCommuneEtablissement=Column(String)
    codeCedexEtablissement=Column(String)
    libelleCedexEtablissement=Column(String)
    codePaysEtrangerEtablissement=Column(String)        
    libellePaysEtrangerEtablissement=Column(String)

    def __repr__(self):
        return f"<AdressePrincipale id={self.siret}>"

class AdresseSecondaire(Base):
    __tablename__ = "AdresseSecondaire"
    id = Column(Integer, primary_key=True, autoincrement=True)
    siret = Column(String)
    complementAdresse2Etablissement=Column(String)
    numeroVoie2Etablissement=Column(String)
    indiceRepetition2Etablissement=Column(String)
    typeVoie2Etablissement=Column(String)
    libelleVoie2Etablissement=Column(String)
    codePostal2Etablissement=Column(String)
    libelleCommune2Etablissement=Column(String)
    libelleCommuneEtranger2Etablissement=Column(String)
    distributionSpeciale2Etablissement=Column(String)
    codeCommune2Etablissement=Column(String)
    codeCedex2Etablissement=Column(String)
    libelleCedex2Etablissement=Column(String)
    codePaysEtranger2Etablissement=Column(String)
    libellePaysEtranger2Etablissement=Column(String)

    def __repr__(self):
        return f"<AdresseSecondaire id={self.siret}>"

class InfoSupplementaire(Base):
    __tablename__ = "InfoSupplementaire"
    id = Column(Integer, primary_key=True, autoincrement=True)
    siret = Column(String, primary_key=True)
    dateDebut=Column(Date)
    etatAdministratifEtablissement=Column(String)
    enseigne1Etablissement=Column(String)
    enseigne2Etablissement=Column(String)
    enseigne3Etablissement=Column(String)
    denominationUsuelleEtablissement=Column(String)
    activitePrincipaleEtablissement=Column(String)
    nomenclatureActivitePrincipaleEtablissement=Column(String)
    caractereEmployeurEtablissement=Column(String)

    def __repr__(self):
        return f"<InfoSpplementaire id={self.siret}>"'''
