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


# Set page config
st.set_page_config(page_title="Instructional Hours Calculator", page_icon="⏰")

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

def parse_time(time_str):
    """Helper to try multiple time formats."""
    for fmt in ('%I:%M%p', '%I:%M %p', '%H:%M'):
        try:
            return datetime.strptime(time_str.strip().lower(), fmt)
        except ValueError:
            continue
    return None

def main():
    st.title("⏰ Instructional Hours Calculator")
    st.markdown("Select class times to calculate apportionment and instructional hours.")

    # 1. Time Selection Inputs
    col1, col2 = st.columns(2)
    with col1:
        # Defaults to 8:00 AM
        start_time = st.time_input("Start Time", value=time(8, 0), step=300)
    with col2:
        # Defaults to 9:50 AM
        end_time = st.time_input("End Time", value=time(9, 50), step=300)

    # 2. Calculate Duration
    # Convert time objects to datetime to perform subtraction
    today = datetime.today()
    start_dt = datetime.combine(today, start_time)
    end_dt = datetime.combine(today, end_time)
    
    # Handle overnight classes (if end time is before start time)
    if end_dt <= start_dt:
        end_dt += timedelta(days=1)
        
    delta = int((end_dt - start_dt).seconds / 60)

    # 3. Validation and Results
    st.divider()

    if delta < 50:
        st.error(f"### {delta} Minutes: Insufficient Time")
        st.info("The 'class hour' (50+ mins) is the basic unit for FTES. (EC 84501)")
    else:
        data = INSTRUCTIONAL_DATA.get(str(delta))
        
        if not data:
            st.warning(f"Duration: {delta} minutes. No exact match found in the lookup table.")
        else:
            # Unpack values safely
            clock = data.get('Clock')
            iH = data.get('iHours')
            brk = data.get('Breaks', 0)
            grey = data.get('grey', False)
            fac = data.get('fac', 0)

            # High-level Metrics
            m1, m2, m3 = st.columns(3)
            m1.metric("Clock Hours", clock)
            m2.metric("Instructional Hours", iH)
            m3.metric("Required Breaks", brk)

            # Details
            if brk > 0:
                st.info(f"💡 **Note:** {brk} break(s) required. Breaks cannot be accumulated.")

            if grey:
                rm = 5 if fac == 10 else 10
                st.warning(f"⚠️ **'Grey' Area Detected**")
                st.write(f"Consider removing **{rm} mins** to exit grey area, or add **{fac} mins** to gain credit.")

    st.sidebar.caption("Reference: T5 57001(e), 58023")
if __name__ == '__main__':
    main()
