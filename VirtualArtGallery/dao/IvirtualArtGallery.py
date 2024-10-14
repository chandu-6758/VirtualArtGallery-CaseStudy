from abc import ABC, abstractmethod
from typing import List
from entity.artwork import Artwork

class IVirtualArtGallery(ABC):

    @abstractmethod
    def addArtwork(self, artwork: Artwork)-> bool:
        pass

    @abstractmethod
    def updateArtwork(self, artwork: Artwork)-> bool:
        pass

    @abstractmethod
    def removeArtwork(self, artwork: Artwork)-> bool:
        pass

    @abstractmethod
    def getArtworkById(self, artworkId: int) -> Artwork:
        pass

    @abstractmethod
    def searchArtworks(self,search_object)-> List[Artwork]:
        pass

    @abstractmethod
    def addArtworkToFavorite(self,userId,artworkId)-> bool:
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self,userId,artworkId)-> bool:
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self,userId)-> List[Artwork]:
        pass