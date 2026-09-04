

doc = Document()

for s in doc.sections:
    s.top_margin = Inches(0.7)
    s.bottom_margin = Inches(0.7)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

for style_name in ["Normal", "Title", "Heading 1", "Heading 2"]:
    st = doc.styles[style_name]
    st.font.name = "Times New Roman"

doc.styles["Normal"].font.size = Pt(11)
doc.styles["Heading 1"].font.size = Pt(15)
doc.styles["Heading 1"].font.bold = True
doc.styles["Title"].font.size = Pt(20)
doc.styles["Title"].font.bold = True

def centered(text, size=11, bold=False, after=8):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(size)
    r.bold = bold
    return p

centered("PROJECT SYNOPSIS", 20, True, 18)
centered("ON", 12, True, 6)
centered("“SMART PARKING AVAILABILITY AND SLOT RECOMMENDATION SYSTEM USING PYTHON”", 17, True, 18)
centered("Mini Project in Python", 13, False, 20)

centered("Submitted By", 12, True, 8)
for i in range(1, 5):
    centered(f"{i}. ______________________________  (Enrollment No. ____________)", 11, False, 4)

centered("BCA – Department of Computer Applications", 12, True, 5)
centered("Vivekananda Institute of Professional Studies (VIPS)", 12, True, 5)
centered("Guru Gobind Singh Indraprastha University", 12, True, 5)
centered("Academic Session 2026–27", 11, False, 10)

doc.add_page_break()

sections = [
("1. TITLE",
"""Smart Parking Availability and Slot Recommendation System Using Python"""),

("2. INTRODUCTION",
"""Finding an available parking space in a crowded college, office, shopping complex or public parking area is often inefficient. Drivers may spend several minutes moving through different lanes looking for an empty slot, resulting in unnecessary fuel consumption, congestion and frustration. Traditional parking systems generally provide only entry and exit control and do not give users a clear real-time view of available spaces.

The proposed Smart Parking Availability and Slot Recommendation System is a Python-based mini-project that digitally maintains parking-slot status and displays available spaces through an interactive dashboard. The system will allow parking slots to be represented individually and marked as Available, Occupied or Reserved. When a vehicle enters or leaves, the corresponding slot status can be updated.

An additional feature of the project is slot recommendation. Instead of simply showing the number of free spaces, the system can recommend a suitable available slot based on factors such as vehicle type, preferred parking zone and distance from the entrance. The project will demonstrate Python programming, data management, search/filtering, basic algorithms and data visualization in a practical real-world application."""),

("3. OBJECTIVES",
"""The major objectives of the project are:

• To develop a digital system for monitoring parking-space availability.
• To display the total, occupied, available and reserved parking slots.
• To maintain parking-slot information in a structured dataset.
• To provide a simple interface for updating vehicle entry and exit.
• To recommend a suitable available parking slot to the user.
• To reduce the time spent searching for parking.
• To generate useful parking statistics such as occupancy rate and peak usage.
• To demonstrate the practical application of Python, data processing and visualization.
• To create a system that can later be connected to sensors or IoT devices."""),

("4. SCOPE OF THE PROJECT",
"""The initial system will be designed for a small-to-medium parking area such as a college campus, office building or shopping complex. It will simulate parking occupancy through manual input or system-generated updates.

The scope includes:

• Creation of parking zones and individual slot IDs.
• Vehicle entry and exit recording.
• Slot status management: Available, Occupied and Reserved.
• Search for available parking spaces.
• Slot recommendation based on predefined rules.
• Vehicle-category support such as car and two-wheeler.
• Dashboard showing occupancy statistics.
• Visual representation of the parking layout.
• Daily/periodic parking usage analysis.
• Basic record storage using CSV/SQLite.

The first version will be a software simulation and will not require physical parking sensors. This keeps the project achievable as a Python mini-project while leaving a clear path for future IoT integration."""),

("5. HARDWARE REQUIREMENTS",
"""Minimum hardware requirements:

• Processor: Intel Core i3 / equivalent or above.
• RAM: 4 GB minimum; 8 GB recommended.
• Storage: At least 500 MB free space.
• Display: 1366 × 768 resolution or above.
• Keyboard and mouse.
• Optional: Internet connection for package installation.
• Future hardware integration: ultrasonic/IR sensors, ESP32/Arduino or Raspberry Pi."""),

("6. SOFTWARE REQUIREMENTS",
"""The proposed software environment is:

• Operating System: Windows 10/11, Linux or macOS.
• Programming Language: Python 3.x.
• IDE/Editor: VS Code, PyCharm or Jupyter Notebook.
• User Interface/Dashboard: Streamlit.
• Data Processing: Pandas and NumPy.
• Visualization: Matplotlib and/or Plotly.
• Database: SQLite for the enhanced version; CSV can be used during initial development.
• Optional future technologies: OpenCV, ESP32/Arduino and IoT communication APIs.

The software stack can be adjusted during implementation depending on the final design and available development time."""),

("7. PROCESS / METHODOLOGY",
"""The project will be developed through the following stages:

1. Requirement Analysis: Identify parking zones, slot categories, vehicle details and information required on the dashboard.
2. System Design: Create the parking-slot structure, status model and recommendation rules.
3. Data Preparation: Build a dataset containing slot ID, zone, vehicle type, status and other relevant fields.
4. Input and Validation: Record vehicle entry/exit and validate slot and vehicle information.
5. Availability Engine: Calculate the number and percentage of available, occupied and reserved spaces.
6. Slot Recommendation: Filter available slots according to vehicle type and user preferences, then rank the suitable slots using a simple scoring/distance rule.
7. Dashboard Development: Present the parking map, counters, tables, filters and charts in an interactive interface.
8. Testing: Test normal entry/exit, full parking, invalid slot selection, reservations and simultaneous status changes.
9. Analysis and Reporting: Generate occupancy trends, peak-hour information and basic parking statistics.
10. Demonstration: Present the working system using a simulated parking environment."""),

("8. PROPOSED SYSTEM FEATURES",
"""The proposed dashboard will contain the following major components:

• Live-style parking overview showing free and occupied slots.
• Color/status indicators for each slot.
• Vehicle entry and exit module.
• Available-slot search.
• Smart slot recommendation.
• Parking-zone filtering.
• Vehicle-type filtering.
• Reservation option in the extended version.
• Occupancy percentage and utilization statistics.
• Peak-hour analysis.
• Searchable parking records.
• Admin-style controls for updating slot status.

For the mini-project demonstration, the system can simulate vehicles entering and leaving so that the dashboard changes immediately without requiring physical sensors."""),

("9. EXPECTED OUTPUT",
"""The final application is expected to display an interactive parking dashboard containing:

• Total number of parking slots.
• Number of currently available slots.
• Number of occupied slots.
• Number of reserved slots.
• Visual parking-slot layout.
• Recommended slot for a selected vehicle.
• Parking occupancy percentage.
• Zone-wise availability.
• Basic charts showing parking usage over time.

Example: If slots A01–A10 are occupied and B01–B10 are available, a user selecting “Car” and “Near Entrance” can receive a recommended free car slot from the appropriate zone instead of manually checking every space."""),

("10. LIMITATIONS",
"""The initial version has several practical limitations:

• Parking status may be updated manually or through simulation rather than physical sensors.
• The recommendation algorithm will be rule-based rather than a highly advanced AI model.
• The system will be designed for a limited parking dataset during the mini-project.
• GPS-level indoor positioning will not be available in the initial version.
• Data security and multi-user authentication may be basic.
• If physical sensors are not connected, the dashboard cannot independently verify whether a real-world slot is occupied.
• The accuracy of the system depends on timely and correct status updates."""),

("11. FUTURE SCOPE",
"""The project can be developed into a real smart-parking platform by integrating IoT hardware and cloud services.

Future enhancements may include:

• Ultrasonic/IR sensors for automatic slot detection.
• ESP32/Arduino/Raspberry Pi integration.
• Real-time cloud synchronization.
• QR-code based parking entry and exit.
• Online slot reservation.
• Digital payment integration.
• Number-plate recognition using computer vision.
• Mobile application for users.
• Dynamic pricing based on parking demand.
• Machine-learning based occupancy and peak-time prediction.
• Navigation to the recommended parking slot.
• Multi-location parking management.
• Admin analytics and automated reports."""),

("12. CONCLUSION",
"""The Smart Parking Availability and Slot Recommendation System provides a practical solution to the everyday problem of finding and managing parking spaces. By combining Python programming, structured data management, an interactive dashboard and a simple recommendation algorithm, the project can show both software-development and analytical skills.

The proposed system is intentionally designed so that it can be completed as a mini-project without expensive hardware. At the same time, its architecture can be extended later with IoT sensors, computer vision, mobile applications and machine learning. Therefore, the project offers a good balance between feasibility for a student team and sufficient scope for future development.""")
]

for heading, body in sections:
    doc.add_heading(heading, level=1)
    for para in body.split("\n\n"):
        if not para.strip():
            continue
        lines = para.split("\n")
        for line in lines:
            line=line.strip()
            if not line:
                continue
            if line.startswith("• "):
                p = doc.add_paragraph(line[2:], style="List Bullet")
            elif len(line) > 2 and line[0].isdigit() and ". " in line[:4]:
                p = doc.add_paragraph(line, style="List Number")
            else:
                p = doc.add_paragraph(line)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(5)

doc.add_page_break()
doc.add_heading("13. TEAM DETAILS AND FACULTY APPROVAL", level=1)
doc.add_paragraph("Project Title: Smart Parking Availability and Slot Recommendation System Using Python")
doc.add_paragraph("Group Members:")
for i in range(1,5):
    doc.add_paragraph(
        f"{i}. Name: ______________________________   Enrollment No.: ____________________",
        style="List Number"
    )
doc.add_paragraph("\nFaculty Guide: ______________________________________________")
doc.add_paragraph("Signature of Faculty Guide: _________________________________")
doc.add_paragraph("\nDate: ____________________")
doc.add_paragraph("Place: ___________________")

doc.save(out)
print(out)
