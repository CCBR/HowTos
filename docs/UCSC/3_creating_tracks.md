# Generating New Tracks

Biowulf/Helix hosts its own instance of the [UCSC Genome Browser](https://hpcnihapps.cit.nih.gov/genome/) which is behind the NIH firewall.

1. Login to VPN
2. Login to the [UCSC Browser website](https://hpcnihapps.cit.nih.gov/genome/cgi-bin/hgSession)
3. Select "My Data > Custom Tracks"
4. Select "Add Custom Tracks"
5. Paste the track data generated in [Creating Track Info](https://ccbr.github.io/HowTos/UCSC/creating_track_info/) into the text box
6. Select "Submit"
7. Review the track information. The column "Error" should be empty. If there is an error then a hyperlink will display "Show" although this often does not contain helpful error information.
8. After troubleshooting any errors select "Go"
9. Use the features at the bottom of the page to alter views and/or add additional track information
10. Select "My Data > My Sessions"
11. Under "Save current settings as named session:" enter a descriptive name of the session
12. Select "Submit"
13. This will move the descriptive name entered into the "session name" list
14. Select the descriptve name, view your track information as saved
15. Copy the hyperlink for this session and share as needed

# Editing a Previous Tracks
1. Login to VPN
2. Login to the [UCSC Browser website](https://hpcnihapps.cit.nih.gov/genome/cgi-bin/hgSession)
3. Select "My Data > My Sessions"
4. Select the descriptve name of the session you'd like to edit
5. Edit the tracks as needed:
    - If wanting to remove or add tracks, then select "My Data > Custom Tracks"; follow steps 5-8 above.
    - If wanting to edit the view of the tracks, follow step 9 above.
10. Select "My Data > My Sessions"
11. Under "Save current settings as named session:" enter a new descriptive name OR the previous name of the session if you'd like to overwrite it
12. Select "Submit"
13. This will move the descriptive name entered into the "session name" list
14. Select the descriptve name, view your track information as saved
15. Copy the hyperlink for this session and share as needed

> TIP: Unindexed file formats like `bed` and `gtf` take significantly longer to load in the genome Browser and it is recommended to convert them to indexed formats like `bigBed` and `bigWig` prior to adding them to your session.
