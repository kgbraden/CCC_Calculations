# -*- coding: utf-8 -*-
"""

#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#
#                                 \\|||||//                                  #
#                                 (  o o  )                                  #
#                ------------Ooo-----(_)--------------------                 #
#                |                                         |                 #
#                |       Programmed by: kale.braden        |                 #
#                |       Date: Sun Mar 22 13:39:54 2026    |                 #
#                |                                         |                 #
#                ------------------------------ooO----------                 #
#                                |___| |___|                                 #
#                                 | |   | |                                  #
#                                 ooO   Ooo                                  #
#~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+#

"""

import streamlit as st
from datetime import datetime, time, timedelta
import json
import base64

# 1. SET PAGE CONFIG (Must be first)
st.set_page_config(
    page_title="CCCCO Hours Calc", 
    page_icon="⏰", 
    layout="centered"
)

# 2. PWA CONFIGURATION
ICON_BASE = "https://raw.githubusercontent.com/kgbraden/CCC_Calculations/main/icon.png"
ICON_URL_V5 = f"{ICON_BASE}?v=5" 
APP_TITLE = "CCCCO Hours Calc"

ICON_URL_V6 = "https://raw.githubusercontent.com/kgbraden/CCC_Calculations/main/icon.png?v=6"
APP_TITLE = "CCCCO Hours Calc"

manifest_dict = {
    "short_name": APP_TITLE,
    "name": APP_TITLE,
    "id": "/cccco-calc-v6", 
    "start_url": ".",
    "display": "standalone",
    "theme_color": "#ffffff",
    "background_color": "#ffffff",
    "icons": [
        {"src": ICON_URL_V6, "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": ICON_URL_V6, "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
    ]
}

manifest_b64 = base64.b64encode(json.dumps(manifest_dict).encode()).decode()

st.markdown(
    f"""
    <script>
        function bruteForceMetadata() {{
            const head = window.parent.document.head;
            
            // 1. Force the Title in 4 different places
            window.parent.document.title = "{APP_TITLE}";
            
            // 2. Set Android-specific metadata (often overrides manifest)
            let metaName = window.parent.document.querySelector("meta[name='application-name']") || document.createElement('meta');
            metaName.name = "application-name";
            metaName.content = "{APP_TITLE}";
            head.appendChild(metaName);

            let mobileCapable = window.parent.document.querySelector("meta[name='mobile-web-app-capable']") || document.createElement('meta');
            mobileCapable.name = "mobile-web-app-capable";
            mobileCapable.content = "yes";
            head.appendChild(mobileCapable);

            // 3. Update Manifest
            const oldManifests = window.parent.document.querySelectorAll("link[rel='manifest']");
            oldManifests.forEach(el => el.remove());
            const newManifest = window.parent.document.createElement('link');
            newManifest.rel = 'manifest';
            newManifest.href = 'data:application/json;base64,{manifest_b64}';
            head.appendChild(newManifest);

            // 4. Update Icons
            const iconTypes = ['icon', 'apple-touch-icon', 'shortcut icon'];
            iconTypes.forEach(t => {{
                let link = window.parent.document.querySelector(`link[rel='${{t}}']`) || window.parent.document.createElement('link');
                link.rel = t;
                link.href = '{ICON_URL_V6}';
                head.appendChild(link);
            }});
        }}

        // Run immediately and every time Streamlit tries to reset the head
        bruteForceMetadata();
        new MutationObserver(bruteForceMetadata).observe(window.parent.document.head, {{ childList: true, subtree: true }});
    </script>
    """,
    unsafe_allow_html=True
)
# Embedded data
INSTRUCTIONAL_DATA = {
    "50": {"Clock": "00:50" , "iHours": 1, "Breaks": 0, "grey": False, "fac": 0},
"55": {"Clock": "00:55" , "iHours": 1, "Breaks": 0, "grey": True, "fac": 10},
"60": {"Clock": "00:60" , "iHours": 1, "Breaks": 0, "grey": True, "fac": 5},
"65": {"Clock": "01:05" , "iHours": 1.3, "Breaks": 0, "grey": False, "fac": 0},
"70": {"Clock": "01:10" , "iHours": 1.4, "Breaks": 0, "grey": False, "fac": 0},
"75": {"Clock": "01:15" , "iHours": 1.5, "Breaks": 0, "grey": False, "fac": 0},
"80": {"Clock": "01:20" , "iHours": 1.6, "Breaks": 0, "grey": False, "fac": 0},
"85": {"Clock": "01:25" , "iHours": 1.7, "Breaks": 0, "grey": False, "fac": 0},
"90": {"Clock": "01:30" , "iHours": 1.8, "Breaks": 0, "grey": False, "fac": 0},
"95": {"Clock": "01:35" , "iHours": 1.9, "Breaks": 0, "grey": False, "fac": 0},
"100": {"Clock": "01:40" , "iHours": 1.9, "Breaks": 1, "grey": True, "fac": 10},
"105": {"Clock": "01:45" , "iHours": 1.9, "Breaks": 1, "grey": True, "fac": 5},
"110": {"Clock": "01:50" , "iHours": 2, "Breaks": 1, "grey": False, "fac": 0},
"115": {"Clock": "01:55" , "iHours": 2, "Breaks": 1, "grey": True, "fac": 10},
"120": {"Clock": "02:0" , "iHours": 2, "Breaks": 1, "grey": True, "fac": 5},
"125": {"Clock": "02:05" , "iHours": 2.3, "Breaks": 1, "grey": False, "fac": 0},
"130": {"Clock": "02:10" , "iHours": 2.4, "Breaks": 1, "grey": False, "fac": 0},
"135": {"Clock": "02:15" , "iHours": 2.5, "Breaks": 1, "grey": False, "fac": 0},
"140": {"Clock": "02:20" , "iHours": 2.6, "Breaks": 1, "grey": False, "fac": 0},
"145": {"Clock": "02:25" , "iHours": 2.7, "Breaks": 1, "grey": False, "fac": 0},
"150": {"Clock": "02:30" , "iHours": 2.8, "Breaks": 1, "grey": False, "fac": 0},
"155": {"Clock": "02:35" , "iHours": 2.9, "Breaks": 1, "grey": False, "fac": 0},
"160": {"Clock": "02:40" , "iHours": 2.9, "Breaks": 2, "grey": True, "fac": 10},
"165": {"Clock": "02:45" , "iHours": 2.9, "Breaks": 2, "grey": True, "fac": 5},
"170": {"Clock": "02:50" , "iHours": 3, "Breaks": 2, "grey": False, "fac": 0},
"175": {"Clock": "02:55" , "iHours": 3, "Breaks": 2, "grey": True, "fac": 10},
"180": {"Clock": "3:00" , "iHours": 3, "Breaks": 2, "grey": True, "fac": 5},
"185": {"Clock": "03:05" , "iHours": 3.3, "Breaks": 2, "grey": False, "fac": 0},
"190": {"Clock": "03:10" , "iHours": 3.4, "Breaks": 2, "grey": False, "fac": 0},
"195": {"Clock": "03:15" , "iHours": 3.5, "Breaks": 2, "grey": False, "fac": 0},
"200": {"Clock": "03:20" , "iHours": 3.6, "Breaks": 2, "grey": False, "fac": 0},
"205": {"Clock": "03:25" , "iHours": 3.7, "Breaks": 2, "grey": False, "fac": 0},
"210": {"Clock": "03:30" , "iHours": 3.8, "Breaks": 2, "grey": False, "fac": 0},
"215": {"Clock": "03:35" , "iHours": 3.9, "Breaks": 2, "grey": False, "fac": 0},
"220": {"Clock": "3:40" , "iHours": 3.9, "Breaks": 3, "grey": True, "fac": 10},
"225": {"Clock": "3:45" , "iHours": 3.9, "Breaks": 3, "grey": True, "fac": 5},
"230": {"Clock": "03:50" , "iHours": 4, "Breaks": 3, "grey": False, "fac": 0},
"235": {"Clock": "03:55" , "iHours": 4, "Breaks": 3, "grey": True, "fac": 10},
"240": {"Clock": "04:00" , "iHours": 4, "Breaks": 3, "grey": True, "fac": 5},
"245": {"Clock": "04:05" , "iHours": 4.3, "Breaks": 3, "grey": False, "fac": 0},
"250": {"Clock": "04:10" , "iHours": 4.4, "Breaks": 3, "grey": False, "fac": 0},
"255": {"Clock": "04:15" , "iHours": 4.5, "Breaks": 3, "grey": False, "fac": 0},
"260": {"Clock": "04:20" , "iHours": 4.6, "Breaks": 3, "grey": False, "fac": 0},
"265": {"Clock": "04:25" , "iHours": 4.7, "Breaks": 3, "grey": False, "fac": 0},
"270": {"Clock": "04:30" , "iHours": 4.8, "Breaks": 3, "grey": False, "fac": 0},
"275": {"Clock": "04:35" , "iHours": 4.9, "Breaks": 3, "grey": False, "fac": 0},
"280": {"Clock": "04:40" , "iHours": 4.9, "Breaks": 4, "grey": True, "fac": 10},
"285": {"Clock": "04:45" , "iHours": 4.9, "Breaks": 4, "grey": True, "fac": 5},
"290": {"Clock": "04:50" , "iHours": 5, "Breaks": 4, "grey": False, "fac": 0},
"295": {"Clock": "04:55" , "iHours": 5, "Breaks": 4, "grey": True, "fac": 10},
"300": {"Clock": "5:00" , "iHours": 5, "Breaks": 4, "grey": True, "fac": 5},
"305": {"Clock": "05:05" , "iHours": 5.3, "Breaks": 4, "grey": False, "fac": 0},
"310": {"Clock": "05:10" , "iHours": 5.4, "Breaks": 4, "grey": False, "fac": 0},
"315": {"Clock": "05:15" , "iHours": 5.5, "Breaks": 4, "grey": False, "fac": 0},
"320": {"Clock": "05:20" , "iHours": 5.6, "Breaks": 4, "grey": False, "fac": 0},
"325": {"Clock": "05:25" , "iHours": 5.7, "Breaks": 4, "grey": False, "fac": 0},
"330": {"Clock": "05:30" , "iHours": 5.8, "Breaks": 4, "grey": False, "fac": 0},
"335": {"Clock": "05:35" , "iHours": 5.9, "Breaks": 4, "grey": False, "fac": 0},
"340": {"Clock": "05:40" , "iHours": 5.9, "Breaks": 5, "grey": True, "fac": 10},
"345": {"Clock": "05:45" , "iHours": 5.9, "Breaks": 5, "grey": True, "fac": 5},
"350": {"Clock": "05:50" , "iHours": 6, "Breaks": 5, "grey": False, "fac": 0},
"355": {"Clock": "05:55" , "iHours": 6, "Breaks": 3, "grey": True, "fac": 10},
"360": {"Clock": "06:00" , "iHours": 6, "Breaks": 3, "grey": True, "fac": 5},
"365": {"Clock": "6.05" , "iHours": 6.3, "Breaks": 5, "grey": False, "fac": 0},
"370": {"Clock": "06:10" , "iHours": 6.4, "Breaks": 5, "grey": False, "fac": 0},
"375": {"Clock": "06:15" , "iHours": 6.5, "Breaks": 5, "grey": False, "fac": 0},
"380": {"Clock": "06:20" , "iHours": 6.6, "Breaks": 5, "grey": False, "fac": 0},
"385": {"Clock": "06:25" , "iHours": 6.7, "Breaks": 5, "grey": False, "fac": 0},
"390": {"Clock": "06:30" , "iHours": 6.8, "Breaks": 5, "grey": False, "fac": 0},
"395": {"Clock": "06:35" , "iHours": 6.9, "Breaks": 5, "grey": False, "fac": 0},
"400": {"Clock": "06:40" , "iHours": 6.9, "Breaks": 6, "grey": True, "fac": 10},
"405": {"Clock": "06:45" , "iHours": 6.9, "Breaks": 6, "grey": True, "fac": 5},
"410": {"Clock": "06:50" , "iHours": 7, "Breaks": 6, "grey": False, "fac": 0},
"415": {"Clock": "06:55" , "iHours": 7, "Breaks": 6, "grey": True, "fac": 10},
"420": {"Clock": "07:00" , "iHours": 7, "Breaks": 6, "grey": True, "fac": 5},
"425": {"Clock": "07:05" , "iHours": 7.3, "Breaks": 6, "grey": False, "fac": 0},
"430": {"Clock": "07:10" , "iHours": 7.4, "Breaks": 6, "grey": False, "fac": 0},
"435": {"Clock": "07:15" , "iHours": 7.5, "Breaks": 6, "grey": False, "fac": 0},
"440": {"Clock": "07:20" , "iHours": 7.6, "Breaks": 6, "grey": False, "fac": 0},
"445": {"Clock": "07:25" , "iHours": 7.7, "Breaks": 6, "grey": False, "fac": 0},
"450": {"Clock": "07:30" , "iHours": 7.8, "Breaks": 6, "grey": False, "fac": 0},
"455": {"Clock": "07:35" , "iHours": 7.9, "Breaks": 6, "grey": False, "fac": 0},
"460": {"Clock": "07:40" , "iHours": 7.9, "Breaks": 7, "grey": True, "fac": 10},
"465": {"Clock": "07:45" , "iHours": 7.9, "Breaks": 7, "grey": True, "fac": 5},
"470": {"Clock": "07:50" , "iHours": 8, "Breaks": 7, "grey": False, "fac": 0},
"475": {"Clock": "07:55" , "iHours": 8, "Breaks": 7, "grey": True, "fac": 10},
"480": {"Clock": "08:00" , "iHours": 8, "Breaks": 7, "grey": True, "fac": 5},
"485": {"Clock": "08:05" , "iHours": 8.3, "Breaks": 7, "grey": False, "fac": 0},
"490": {"Clock": "08:10" , "iHours": 8.4, "Breaks": 7, "grey": False, "fac": 0},
"495": {"Clock": "08:15" , "iHours": 8.5, "Breaks": 7, "grey": False, "fac": 0},
"500": {"Clock": "08:20" , "iHours": 8.6, "Breaks": 7, "grey": False, "fac": 0},
"505": {"Clock": "08:25" , "iHours": 8.7, "Breaks": 7, "grey": False, "fac": 0},
"510": {"Clock": "08:30" , "iHours": 8.8, "Breaks": 7, "grey": False, "fac": 0},
"515": {"Clock": "08:35" , "iHours": 8.9, "Breaks": 7, "grey": False, "fac": 0},
"520": {"Clock": "08:40" , "iHours": 8.9, "Breaks": 8, "grey": True, "fac": 10},
"525": {"Clock": "08:45" , "iHours": 8.9, "Breaks": 8, "grey": True, "fac": 5},
"530": {"Clock": "08:50" , "iHours": 9, "Breaks": 8, "grey": False, "fac": 0},
"540": {"Clock": "09:00" , "iHours": 9, "Breaks": 8, "grey": True, "fac": 5},

}

def main():
    st.title("⏰ CCCCO Hours Calculator")
    st.markdown("Select class times to calculate apportionment and instructional hours.")

    # Time Selection
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            start_time = st.time_input("Start Time", value=time(8, 0), step=300)
        with col2:
            end_time = st.time_input("End Time", value=time(9, 50), step=300)

    # Calculation
    today = datetime.today()
    start_dt = datetime.combine(today, start_time)
    end_dt = datetime.combine(today, end_time)
    
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
        
    delta = int((end_dt - start_dt).seconds / 60)

    st.divider()

    if delta < 50:
        st.error(f"### {delta} Minutes: Insufficient Time")
        st.info("The 'class hour' (50+ mins) is the basic unit for FTES. (EC 84501)")
    else:
        data = INSTRUCTIONAL_DATA.get(str(delta))
        
        if not data:
            st.warning(f"Duration: {delta} minutes. No exact match found in lookup table.")
            st.caption("Common increments are every 5 minutes.")
        else:
            # Metrics
            m1, m2, m3 = st.columns(3)
            m1.metric("Clock Hours", data['Clock'])
            m2.metric("Instructional Hours", f"{data['iHours']:.1f}")
            m3.metric("Required Breaks", data['Breaks'])

            # Detailed Logic
            if data['Breaks'] > 0:
                st.info(f"💡 **Note:** {data['Breaks']} break(s) required."+\
                         "         The 10-minute break time permitted in each clock hour may not be \n"+ \
                         "         accumulated during a multiple hour class to be taken at end of the \n"+ \
                         "         class and be counted for FTES apportionment. "+ \
                         "         Reference: T5 58023.")

            if data['grey']:
                rm = 5 if data['fac'] == 10 else 10
                st.warning("⚠️ **'Grey' Area Detected**")
                st.markdown(f"""
                This duration is inefficient for apportionment:
                * **To gain credit:** Add **{data['fac']} mins**
                * **To exit grey area:** Remove **{rm} mins**
                """)

    # --- SIDEBAR TOOLS ---
    with st.sidebar:
        
        """
        st.header("App Settings")
        if st.button("🧹 Clear App Cache"):
            st.markdown('<script>window.clearPWAData();</script>', unsafe_allow_html=True)
        
        st.info("If you see the Streamlit icon, click 'Clear App Cache', delete the shortcut from your home screen, and re-install.")
        
        st.divider()
        """
        st.info("Programmed by Kale Braden, San Joaquin Delta College")
        st.divider()
        st.caption("Reference: T5 57001(e), 58023")

if __name__ == '__main__':
    main()