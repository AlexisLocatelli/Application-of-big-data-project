from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models
from schemas import EtablissementInfo, AdressePrincipale, AdresseSecondaire, InfoSupplementaire

app = FastAPI()

db=SessionLocal()

@app.get("/")
def home():
    return {"message": "Hello World, the app was loaded successfully"}

@app.get("/EtablissementInfo", response_model=List[EtablissementInfo], status_code=200)
def get_all_etablissementInfo():
    all_etablissement=db.query(models.EtablissementInfo).all()
    return all_etablissement

@app.get("/EtablissementInfo/{siret_id}", response_model=List[EtablissementInfo], status_code=status.HTTP_200_OK)
def get_etablissements_by_siret(siret_id: str):
    etablissements = db.query(models.EtablissementInfo).filter(models.EtablissementInfo.siret == siret_id).all()

    if not etablissements:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Etablissement not found")

    return [EtablissementInfo.from_orm(etablissement) for etablissement in etablissements]


@app.post("/EtablissementInfo", response_model=EtablissementInfo, status_code=status.HTTP_201_CREATED)
def create_an_item(EtablissementInfo: EtablissementInfo):

    db_item=db.query(models.EtablissementInfo).filter(models.EtablissementInfo.siret==EtablissementInfo.siret).first()

    if db_item is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Etablissement already exists")

    new_etablissement=models.EtablissementInfo(
        id=EtablissementInfo.id,
        siren=EtablissementInfo.siren,
        nic=EtablissementInfo.nic,
        siret=EtablissementInfo.siret,
        statutDiffusionEtablissement=EtablissementInfo.statutDiffusionEtablissement,
        dateCreationEtablissement=EtablissementInfo.dateCreationEtablissement,
        trancheEffectifsEtablissement=EtablissementInfo.trancheEffectifsEtablissement,
        anneeEffectifsEtablissement=EtablissementInfo.anneeEffectifsEtablissement,
        activitePrincipaleRegistreMetiersEtablissement=EtablissementInfo.activitePrincipaleRegistreMetiersEtablissement,
        dateDernierTraitementEtablissement=EtablissementInfo.dateDernierTraitementEtablissement,
        etablissementSiege=EtablissementInfo.etablissementSiege,
        nombrePeriodesEtablissement=EtablissementInfo.nombrePeriodesEtablissement,            
        )

    db.add(new_etablissement)
    db.commit()

    return new_etablissement


@app.put("/EtablissementInfo/{siret_id}", response_model=EtablissementInfo, status_code=status.HTTP_200_OK)
def update_an_item(siret_id: str, EtablissementInfo: EtablissementInfo):
    etablissement_to_update=db.query(models.EtablissementInfo).filter(models.EtablissementInfo.siret==siret_id).first()

    if etablissement_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Etablissement not found")

    etablissement_to_update.siren=EtablissementInfo.siren
    etablissement_to_update.nic=EtablissementInfo.nic
    etablissement_to_update.siret=EtablissementInfo.siret
    etablissement_to_update.statutDiffusionEtablissement=EtablissementInfo.statutDiffusionEtablissement
    etablissement_to_update.dateCreationEtablissement=EtablissementInfo.dateCreationEtablissement
    etablissement_to_update.trancheEffectifsEtablissement=EtablissementInfo.trancheEffectifsEtablissement
    etablissement_to_update.anneeEffectifsEtablissement=EtablissementInfo.anneeEffectifsEtablissement
    etablissement_to_update.activitePrincipaleRegistreMetiersEtablissement=EtablissementInfo.activitePrincipaleRegistreMetiersEtablissement
    etablissement_to_update.dateDernierTraitementEtablissement=EtablissementInfo.dateDernierTraitementEtablissement
    etablissement_to_update.etablissementSiege=EtablissementInfo.etablissementSiege
    etablissement_to_update.nombrePeriodesEtablissement=EtablissementInfo.nombrePeriodesEtablissement

    db.commit()

    return etablissement_to_update


@app.delete("/EtablissementInfo/{siret_id}")
def delete_item(siret_id: str):
    item_to_delete=db.query(models.EtablissementInfo).filter(models.EtablissementInfo.siret==siret_id).first()
    
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Etablissement not found")
    
    db.delete(item_to_delete)
    db.commit()

    return {"message": "Item deleted successfully"}