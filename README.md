# HomeBrew

## Beschreibung
Software zur steuerung einer Brauanlage.
Misst tie Temperatur, regelt die Heizplatte und steuert die Rührgescwindigkeit des Motors

## Software Komponenten
### sync.sh
Bash script um den neusten sourcecode von GitHub zu clonen und den alten (falls vorhanden) zu löschen.

### config.sh
Dieses script muss einmalig ausgeführt werden.
Es instaliert alle nötigen Softwarekomponenten und Python libraries

### homebrew (Ordner)
Hier befinden sich die verschiedenen Softwarekomponenten der Brausteuerung
