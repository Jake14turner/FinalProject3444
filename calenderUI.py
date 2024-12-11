from user import initializeUserInfoJSON
import streamlit as st
import json

def generateCalanderUI(username):
    data = st.session_state.data


    calendarHTML = f"""
            <style>
            :root {{
                --primary-clr: #EF4F07;
            }}
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: "Poppins" , sans-serif;
            }}
            body {{
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #FBAB7E;
                background-image: linear-gradient(151deg, #FBAB7E 0%, #F7CE68 33%, #ffa22e 66%, #fa691b 100%);


            }}
            .container{{
                position: relative;
                width: 1200px;
                min-height: 850px;
                margin: 0 auto;
                padding: 5px;
                color: #9F0B0B;
                display: flex;
                border-radius: 10px;
                bbackground-color: #ff8928;
                background-image: #36454F;

            }}
            .left {{
                width: 60%;
                padding: 20px;
            }}
            .calendar {{
                position: relative;
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                flex-wrap: wrap;
                justify-content: space-between;
                color: #290855;
                border-radius: 5px;
                background-color: #FAE8D6;
                
                
;
            }}
            .calendar::before, 
            .calendar::after {{
                content: "";
                position: absolute;
                top: 50%;
                left: 100%;
                width: 12px;
                height: 97%;
                border-radius: 0 5px 5px 0;
                background-color: #F8894B;
                transform: translateY(-50%);
            }}
            .calendar::before {{
                height: 94%;
                left: calc(100% + 12px);
                background-color: #F25F06;
            }}
            .calendar .month{{
                width: 100%;
                height: 150px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 50px;
                font-size: 1.2rem;
                font-weight: 650;
                text-transform: UPPERCASE;
                color: #CC5803;
            }}
            .calendar .month .prev,
            .calendar .month .next {{
                cursor: pointer;
            }}
            .calendar .month .prev:hover,
            .calendar .month .next:hover {{
                color: var(--primary-clr);
            }}
            .calendar .weekdays {{
                width: 100%;
                height: 100px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 20px;
                font-size: 1rem;
                font-weight: 700;
                text-transform: capitalize;
                color: #CC5803;
            }}
            .calendar .weekdays div {{
                width: 14.28%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .calendar .days {{
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                padding: 0 20px;
                font-size: 1rem;
                font-weight: 500;
                margin-bottom: 20px;
            }}
            .calendar .days .day {{
                width: 14.28%;
                height: 90px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                color: var(--primary-clr);
                border: 0.5px solid #FAD6C6;
            }}
            .calendar .day:not(.prev-date , .next-date):hover {{
                color : #fff;
                background-color: var(--primary-clr);
            }}
            .calendar .days .prev-date,
            .calendar .days .next-date {{
                color: #592404;
            }}
            .calendar .days .active {{
                position: relative;
                font-size: 2.2rem;
                color:#F4FDFF;
                background-color: var(--primary-clr);
            }}
            .calendar .days .active::before {{
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
               box-shadow: 0 0 10px 2px rgba(239, 79, 7, 0.5);

            }}
            .calendar .days .today {{
                font-size: 2.2rem;
                color: D55100;
            }}
            .calendar .days .event {{
                position: relative;
            }}
            .calendar .days .event::after {{
                content: ''; 
                position: absolute;
                bottom: 10%;
                left: 50%;
                width: 75%;
                height: 4px;
                border-radius: 20px;
                transform: translateX(-50%);
                background-color: var(--primary-clr);
            }}
            .calendar .event:hover::after {{
                background-color: #FCFAD7;
            }}
            .calendar .active.event::after {{
                background-color: #FCFAD7;
                bottom: 20%;
            }}
            .calendar .active.event{{
                padding-bottom: 10px;
            }}
            .calendar .goto-today {{
                width: 100%;
                height: 60px;   
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 5px;
                padding: 0 20px;
                margin-bottom: 20px;
                color: var(--primary-clr);
            }}
            .calendar .goto-today .goto {{
                display: flex;
                align-items: center;
                border-radius: 5px;
                overflow: hidden;
                border: 1px solid var(--primary-clr);
            }}
            .calendar .goto-today .goto input {{
                width: 100%;
                height: 30px;   
                outline: none;
                border: none;
                border-radius: 5px;
                padding: 0 20px;
                color: var(--primary-clr);
                border-radius: 5px;
            }}
            .calendar .goto-today button {{
                padding: 8px 10px;
                border: 1px solid var(--primary-clr);
                border-radius: 5px;
                background-color: transparent;
                cursor: pointer;
                color: var(--primary-clr);
            }}
            .calendar .goto-today button:hover {{
                color: #FCFAD7;
                background-color: var(--primary-clr);
            }}
            .calendar .goto-today .goto button {{
                border: none;
                border-left: 1px solid var(--primary-clr);
                border-radius: 0;
            }}
            .container .right {{
                position: relative;
                width: 40%;
                min-height:100%;
                padding: 20px 0;

            }}
            .right .today-date{{
                width:100%;
                height:50px;
                display:flex;
                flex-wrap:wrap;
                gap:10px;
                align-items:center;
                justify-content:space-betwen;
                padding: 0 40px;
                padding-left: 70px;
                margin-top:50px;
                margin-bottom:20px;
                text-transform: capitalize;
                color: #CC5803;

            }}
            .today-date .even-day{{
                font-size: 1.2rem;
                font-weight: 500;
            }}
            .today-date .event-date{{
                font-size:1.2rem;
                font-weight: 500;
                color:#7C3205;
            }}
            .events{{
                width:100%;
                height:100%;
                max-height:600px;
                overflow-x: hidden;
                overflow-y:auto;
                display:flex;
                flex-direction:column;
                padding:4px;
            }}
            .events .event{{
                position: relative;
                width: 95%;
                min-height: 70px;
                display: flex;
                justify-content: center;
                flex-direction: column;
                gap: 5px;
                padding: 0 20px;
                padding-left: 50px;
                color: #FC6B14;
                cursor: pointer;
                background: linear-gradient(90deg,#FC6B14,transparent);
            }}
            .events .event:nth-child(even){{
                background:transparent;
            }}
            .events .event:hover{{
                background: linear-gradient(70deg,var(--primary-clr),transparent);
            }}
            .events .event .title{{
                display: flex;
                align-items: center;
                pointer-events: none;
            }}
            .events .event .title .event-title{{
                font-size: 1rem;
                font-weight: 450;
                margin-left: 15px;
                color: #111110;
            }}
            .events .event .title i{{
            color: var(--primary-clr);
            font-size: 0.6rem;
            }}
            .events .event:hover .title i,
            .events .event:hover .event-time{{
                color:#fff;
            }}
            .events .event .event-time{{
                font-size: 0.8rem;
                font-weight: 400;
                color: #FCF0E9;
                margin-left: 15px;
                pointer-events: none;

            }}
            .events .event::after{{
                content: 2713;
                position: absolute;
                top: 50%;
                right: 0;
                font-size: 3rem;
                display:none;
                align-items: center;
                opacity: 0.3;
                color: FCF2EB;
                transform: translateY(-50%);


            }}
            .events .event:hover::after{{
                display:flex;
            }}
            .events .no-event{{
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.5rem;
                font-weight: 500;
                color: #FCF0E9;
            }}
            .event .fas.fa-circle {{
                font-size: 0.6rem;
                color: #FFFFFF; 
                margin-right: 8px; 
                vertical-align: middle;
            }}

            .add-event-wrapper{{
                position: absolute;
                bottom: 100px;
                left: 50%;
                width:90%;
                max-height:0;
                overflow:hidden;
                border-radius: 5px;
                background-color: #FBAB7E;
                background-image: linear-gradient(62deg, #FBAB7E 0%, #F7CE68 100%);

                transform: translateX(-50%);
                transition: max-height 0.5s;
            }}
            .add-event-wrapper.active{{
                max-height: 300px;
            }}
            
            .add-event-header{{
                width: 100%;
                height: 50px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 20px;
                color:#FFFFFF;
                border-bottom:1px solid #f5f5f5 ;

            }}
            .add-event-header .close{{
                font-size: 1.5rem;
                cursor: pointer;
            }}
            .add-event-header .close:hover{{
                color:var(--primary-clr);
            }}
            .add-event-header .title{{
                font-size:1.2rem;
                font-weight: 500;
            }}
            .add-event-body{{
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                gap: 5px;
                padding: 20px;
            }}
            .add-event-body .add-event-input{{
                width: 100%;
                height: 40px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 10px;
            }}
            .add-event-body .add-event-input input {{
                width:100%;
                height: 100%;
                outline:none;
                border: none;
                border-bottom:1px solid #f5f5f5;
                padding: 0 10px;
                font-size: 1rem;
                font-weight: 400;
                color: var(--primary-clr);
            }}
            .add-event-body .add-event-input input::placeholder{{
                color: #F8CCB3;
            }}
            .add-event-body .add-event-input input:focus{{
                border-color: var(--primary-clr);
            }}
            .add-event-body .add-event-input input:focus::placeholder{{
                color: var(--primary-clr);
            }}
            .add-event-footer{{
                display: flex;
                align-items:center;
                justify-content: center;
                padding: 20px;
            }}
            .add-event-btn{{
                height: 40px;
                font-size: 1rem;
                font-weight: 500;
                outline: none;
                border:none;
                color:#fff;
                background-color: var(--primary-clr);
                border-radius: 5px;
                cursor: pointer;
                padding: 5px 10px;
                border: 1px solid var(--primary-clr);
            }}
            .add-event-btn:hover{{
                color:var(--primary-clr);
                background-color: transpent;
            }}
            .add-event{{
                position: absolute;
                bottom: 30px;
                right: 30px;
                width: 40px;
                height: 40px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1rem;
                color: ##111110;
                border: 5px solid #111110;
                opacity: 0.5;
                border-radius: 50%;
                background-color: transparent;
                cursor:pointer;

            }}
            .add-event:hover{{
                opacity:1;
            }}
            .add-event i{{
                pointer-events:none;
            }}
            @media (max-width : 1000px) {{
                body{{
                    align-items: flex-start;
                    justify-content: flex-start;
                }}
                .container{{
                    min-height: 100vh;
                    flex-direction: column;
                    border-radius: 0;
                }}
                .container .left ,
                .container .right{{
                    width: 100%;
                    height: 100%;
                    padding: 20 0;
                }}
                .calendar::before,
                .calendar::after{{
                    top: 100%;
                    left: 50%;
                    width: 97%;
                    height: 12px;
                    border-radius: 0 0 5px 5px;
                    transform: translateX(-50%);
                }}
                .calendar::before{{
                    width: 94%;
                    top: calc(100% + 12px);
                }}
                .events{{
                    padding-bottom: 340px;
                }}
                .add-event-wrapper{{
                    bottom: 100px;
                }}
            }}
            @media (max-width : 500px){{
                .calendar .month{{
                    height: 75px;
                }}
                .calendar .weekdays {{
                    height: 50px;
                }}
                .calendar .days .day{{
                    height: 40px;
                    font-size: 0.8rem;
                }}
                .calendar .days .day.active,
                .calendar .days .day.today{{
                    font-size: 1rem;
                }}
                .right .today-date{{
                    padding: 20px;
                }}
            }}
            </style>


            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <link rel="stylesheet" type="text/css" href="style.css"  />
                <link
                rel="stylesheet" 
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" 
                integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" 
                crossorigin="anonymous" 
                referrerpolicy="no-referrer" />
                <title>Calander</title>
            </head>  
            <body>
                <div class="container">
                <div class="left">
                    <div class="calendar">
                    <div class="month">
                        <i class="fa fa-angle-left prev"></i>
                            <div class="date"></div>
                        <i class="fa fa-angle-right next"></i>
                    </div>
                    <div class="weekdays">
                        <div>sun</div>
                        <div>mon</div>
                        <div>tue</div>
                        <div>wed</div>
                        <div>thur</div>
                        <div>fri</div>
                        <div>sat</div>
                    </div>
                    <div class="days">
                        
                    </div>
                    <div class="goto-today">
                        <div class="goto">
                        <input type="text" placeholder="mm/yyyy" class="date-input" >
                        <button class="goto-btn">go</button>
                        </div>
                        <button class="today-btn">today</button>
                    </div>
                    </div>
                </div>
                <div class ="right">
                    <div class="today-date">
                    <div class="event-day">wed</div>
                    <div class="event-date">16 November 2022</div>
                    </div>
                    <div class="events">                             
                    </div>
                    <div class="add-event-wrapper  ">

                        <div class="add-event-header">
                        <div class="title">Add Event</div>
                        <i class="fas fa-times close"></i>
                        
                        </div>

                        <div class="add-event-body">
                        <div class="add-event-input">
                            <input 
                            type="text" 
                            placeholder="Event Name" 
                            class="event-name">
                        </div>
                        <div class="add-event-input">
                            <input 
                            type="text" 
                            placeholder="Event Time From" 
                            class="event-time-from">
                        </div>
                        <div class="add-event-input">
                            <input 
                            type="text" 
                            placeholder="Event Time To" 
                            class="event-time-to">
                        </div>
                        <div class="add-event-footer">
                            <button class="add-event-btn">add event</button>
                        </div>
                        </div>
                    </div>
                    <button class ="add-event">
                        <i class="fas fa-plus"></i>
                    </button>
                </div>
                </div>
                <script src="script.js"></script>
            </body>
            </html> 
            

            <script>
            const calendar = document.querySelector(".calendar"),
            date = document.querySelector(".date"),
            daysContainer = document.querySelector(".days"),
            prev = document.querySelector(".prev"),
            next = document.querySelector(".next");
            todayBtn = document.querySelector(".today-btn"),
            gotoBtn = document.querySelector(".goto-btn"),
            dateInput = document.querySelector(".date-input"),
            eventDay = document.querySelector(".event-day"),
            eventDate = document.querySelector(".event-date"),
            eventsContainer = document.querySelector(".events"),
            addEventSubmit = document.querySelector(".add-event-btn");
            let today = new Date();
            let activeDay;
            let month = today.getMonth();
            let year = today.getFullYear();
            const months =[
                "January", 
                "February", 
                "March", 
                "April", 
                "May", 
                "June", 
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ];
            //set a empty array 
            let eventsArr = [];
            //create an array to store all of the assignments
        const assignmentsArray = [];
            //then call get
           // getEvents();
            // Convert assignments into events for the calendar
// Convert assignments into events for the calendar
// Load events from localStorage once on page load
        document.addEventListener("DOMContentLoaded", () => {{
            getEvents(); // Load any saved events from localStorage
            
            // Populate assignmentsArray with data from the backend
            populateAssignmentsArray(); 
            addAssignmentsToEvents(); // Add assignments to eventsArr, avoiding duplicates
            initCalendar(); // Initialize the calendar to display events
        }});

        // Function to load events from localStorage
        function getEvents() {{
            eventsArr = []; // Start fresh to prevent duplicate entries each session
            const storedEvents = localStorage.getItem("events");
            if (storedEvents) {{
                eventsArr.push(...JSON.parse(storedEvents));
            }}
        }}

        // Function to populate assignmentsArray from backend data
        function populateAssignmentsArray() {{
            
            const data = {json.dumps(data)};

            // Parse and populate assignmentsArray
            data.courses.forEach(course => {{
                course.assignments.forEach(assignment => {{
                    const individualAssignment = new Assignment(assignment.name, assignment.due_date);
                    assignmentsArray.push(individualAssignment);
                }});
            }});
        }}

        class Assignment {{
                constructor(name, dueDate) {{
                this.name = name;
                this.dueDate = dueDate;
                }}
            }}

        


            

     

   // Function to add assignments to eventsArr, avoiding duplicates
        function addAssignmentsToEvents() {{
            assignmentsArray.forEach(assignment => {{
                const dueDate = new Date(assignment.dueDate);
                const day = (dueDate.getUTCDate()-1);
                const month = dueDate.getUTCMonth() + 1; // JavaScript months are 0-indexed
                const year = dueDate.getUTCFullYear();
                
                const newEvent = {{
                    title: assignment.name,
                    time: "Due Date"
                }};

                // Check if an event already exists for this date in eventsArr
                let dayExists = false;
                eventsArr.forEach(eventObj => {{
                    if (eventObj.day === day && eventObj.month === month && eventObj.year === year) {{
                        if (!eventObj.events.some(event => event.title === assignment.name)) {{
                            eventObj.events.push(newEvent); // Add only if not already present
                        }}
                        dayExists = true;
                    }}
                }});

                // If no events exist for this day, create a new entry
                if (!dayExists) {{
                    eventsArr.push({{
                        day: day,
                        month: month,
                        year: year,
                        events: [newEvent]
                    }});
                }}
            }});

            // Save events to localStorage after adding assignments only once
            saveEvents();
        }}

        // Function to save events to localStorage
        function saveEvents() {{
            localStorage.setItem("events", JSON.stringify(eventsArr));
        }}

            // function to add days
            function initCalendar(){{
                //first day of the month
                const firstDay = new Date(year, month, 1);
                //last day of the month, 0 mean the last day of the previous month-current month
                const lastDay = new Date(year, month+1, 0);
                //last day of previous month because O automatically set it to last day of previous month
                const prevLastDay = new Date(year, month, 0);
                //Number of days in the previous month
                const prevDays = prevLastDay.getDate();
                //Number of days in the current month
                const LastDate = lastDay.getDate();
                // Day of the week the month starts on
                const day = firstDay.getDay();
                //  Remaining days for next month
                const nextDays = 7 - lastDay.getDay()-1;
            //update date to top of calendar
            date.innerHTML =months[month] +" "+ year; 
            //adding days on dom
            let days = "";
            //prev month days
            for (let x= day; x > 0;x--){{
                //The class day is used to style all days, and prev-date can be used to style days from the previous month
                days +=`<div class= "day prev-date" >${{prevDays - x + 1}}</div>`;
            }}
            //current month days
            for (let i=1; i <= LastDate; i++){{
                let event = false;
                eventsArr.forEach((eventObj)=>{{
                if(
                    eventObj.day ===i &&
                    eventObj.month === month +1 &&
                    eventObj.year === year

                ){{
                    //if event found
                    event =true;
                }}
                }});
                //if day is today add class today
                if (i === new Date().getDate() && 
                year === new Date().getFullYear()&& 
                month === new Date().getMonth() 
                ){{
                    activeDay = i;
                    getActiveDay(i);
                    updateEvents(i);
                    //if event found also add event class
                    //add active on today at startup
                    if (event){{
                    days +=`<div class= "day today active event" >${{i}}</div>`;        
                }}
                else{{
                    days +=`<div class= "day active today" >${{i}}</div>`;
                    
                }}
                }}
                // add remaining as it is
                else{{
                    if(event){{
                        days += `<div class ="day event">${{i}}</div>`;
                    }} else{{
                    days += `<div class ="day">${{i}}</div>`;
                }}
                }}
            }}
            //next  month days
            for(let j =1; j <= nextDays; j++){{
                days +=`<div class="day next-date" >${{j}}</div>`;
            }}
            daysContainer.innerHTML = days;
            //add listener after calender initialized
            addListner();
            }}
            initCalendar();
            //prev month 
            function prevMonth(){{
                month--;
                if(month <0){{
                    month = 11;
                    year--;
                }}
                initCalendar();

            }}
            // next month
            function nextMonth(){{
                month++;
                if (month > 11){{
                    month = 0;
                    year++;
                }}
                initCalendar();
            }}
            //add eventListnner on prev and next
            prev.addEventListener("click",prevMonth);
            next.addEventListener("click", nextMonth);
            // lets add togo date and goto today functionality
            todayBtn.addEventListener("click", ()=>{{
                today = new Date();
                month = today.getMonth();
                year = today.getFullYear();
                initCalendar();
            }});
            dateInput.addEventListener("input",(e)=>{{
                dateInput.value = dateInput.value.replace(/[^0-9/]/g,"");
                if (dateInput.value.length ===2){{
                    dateInput.value +="/";

                }}
                if (dateInput.value.lenth >7){{
                    // don't allow more than 7 character
                    dateInput.value = dateInput.value.slice(0,7);
                }}
                //if backspace pressed
                if(e.inputType ==="deleteContentBackward"){{
                    if(dateInput.value.length === 3){{
                        dateInput.value = dateInput.value.slice(0,2);
                    }}
                }}

            }});
            gotoBtn.addEventListener("click", gotoDate);
            //function to go to entered date
            function gotoDate(){{
                const dateArr = dateInput.value.split("/");
                //some data validation
                if(dateArr.length ===2){{
                    if(dateArr[0]>0 && dateArr[0]<13 && dateArr[1].length ===4){{
                        month = dateArr[0]-1;
                        year = dateArr[1];
                        initCalendar();
                        return;
                    }}
                }}
                //if invalid date
                alert("invalid date");
            }}
            const addEventBtn =document.querySelector(".add-event"),
            addEventContainer =document.querySelector(".add-event-wrapper"),
            addEventCloseBtn =document.querySelector(".close"),
            addEventTitle =document.querySelector(".event-name"),
            addEventFrom =document.querySelector(".event-time-from"),
            addEventTo =document.querySelector(".event-time-to");
            addEventBtn.addEventListener("click",()=>{{
            addEventContainer.classList.toggle("active");
            }});
            addEventCloseBtn.addEventListener("click", ()=>{{
                addEventContainer.classList.remove("active");
            }})
            document.addEventListener("click",(e)=>{{
                // if(e.target !== addEventBtn && !addEventCloseBtn.contains(e.target))
                //    addEventContainer.classList.remove("active");
                if (!addEventContainer.contains(e.target) && e.target !== addEventBtn) {{
                    addEventContainer.classList.remove("active");
                }}
            }});
            //allow only 50 chars in title
            addEventTitle.addEventListener("input",(e)=>{{
                addEventTitle.value = addEventTitle.value.slice(0,50);
            }});
            //time format in from and to time 
            addEventFrom.addEventListener("input",(e)=>{{
                //remove anything else nubers
                addEventFrom.value = addEventFrom.value.replace(/[^0-9:]/g,"");
                //if two numbers enter auto add:
                if(addEventFrom.value.length ===2){{
                    addEventFrom.value +=":";
                    }}
                if (addEventFrom.value.length >5){{
                    addEventFrom.value = addEventFrom.value.slice(0,5);
                }}
            }});
            addEventTo.addEventListener("input",(e)=>{{
                //remove anything else nubers
                addEventTo.value = addEventTo.value.replace(/[^0-9:]/g,"");
                //if two numbers enter auto add:
                if(addEventTo.value.length ===2){{
                    addEventTo.value +=":";
                    }}
                if (addEventTo.value.length >5){{
                    addEventTo.value = addEventFrom.value.slice(0,5);
                }}
            }});
            //create function to add listener on days after rendered
            function addListner(){{
                const days = document.querySelectorAll(".day");
                days.forEach((day)=>{{
                    day.addEventListener("click", (e)=>{{
                        activeDay =Number(e.target.innerHTML)
                        //call active day after click
                        getActiveDay(e.target.innerHTML);
                        updateEvents(Number(e.target.innerHTML));
                        //remove active from already active day
                        days.forEach((day)=>{{
                            day.classList.remove("active");
                        }});
                        //if prev month day clicked goto prev month and add acive
                    if(e.target.classList.contains("prev-date")){{
                        prevMonth();
                        setTimeout(() => {{
                            //select all days of that month
                            const days =document.querySelectorAll(".day");
                            //after going to prevmonth and active to clicked
                            days.forEach((day)=>{{
                                if(!day.classList.contains("prev-date")&&
                                day.innerHTML===e.target.innerHTML){{
                                    day.classList.add("active");
                                }}
                            }});
                        }},100);
                    //same with next month days
                    }} else if(e.target.classList.contains("next-date")){{
                        nextMonth();
                        setTimeout(() => {{
                            //select all days of that month
                            const days =document.querySelectorAll(".day");
                            //after going to nextmonth and active to clicked
                            days.forEach((day)=>{{
                                if(!day.classList.contains("next-date")&&
                                day.innerHTML===e.target.innerHTML){{
                                    day.classList.add("active");
                                }}
                            }});
                        }},100);
                    }}
                    else{{
                        //remaining current month days
                        e.target.classList.add("active");
                    }}
                    }});
                }});
            }}



            //show active day events and date at top

            function getActiveDay(date){{
                const day = new Date(year , month , date);
                const dayName = day.toString().split(" ")[0];
                eventDay.innerHTML = dayName;
                eventDate.innerHTML = date + " " + months[month] + " " + year;
            }}

            //function to show events of that day
            function updateEvents(date){{
                let events = "";
                eventsArr.forEach((event) => {{
                    //get events of active day only
                    if(
                        date == event.day &&
                        month + 1 == event.month && 
                        year == event.year 
                    ){{
                        //then show event on document
                        event.events.forEach((event) => {{
                            events += `
                            <div class="event">
                                <div class="title">
                                    <i class="fas fa-circle"></i>
                                    <h3 class="event-title">${{event.title}}</h3>
                                </div>
                                <div class="event-time">
                                    <span class="event-time">${{event.time}}</span>
                                </div>
                            </div>
                            `;
                        }});
                    }}
                }})
                //if nothing found
                if((events == "")){{
                    events =`<div class="no-event">
                                <h3>No Events</h3>
                            </div>`;
                }}
                eventsContainer.innerHTML = events;
                //save events when update events called
                saveEvents();
            }}

            //create function to add events
            addEventSubmit.addEventListener("click" , () => {{
                const eventTitle = addEventTitle.value;
                const eventTimeFrom = addEventFrom.value;
                const eventTimeTo = addEventTo.value;
                //some validations
                if(eventTitle == "" || eventTimeFrom == "" || eventTimeTo == ""){{
                    alert("Please fill all the fields.");
                    return;
                }}
                const timeFromArr = eventTimeFrom.split(":");
                const timeToArr = eventTimeTo.split(":");
                if(
                    timeFromArr.length !== 2 || timeToArr.length !== 2 || 
                    timeFromArr[0] > 23 || timeFromArr[1] > 59 ||
                    timeToArr[0] > 23 || timeToArr[1] > 59
                ){{
                    alert("Invalid Time Format.");
                }}
                const timeFrom = convertTime(eventTimeFrom);
                const timeTo = convertTime(eventTimeTo);
                const newEvent = {{
                    title : eventTitle,
                    time : timeFrom + " - " + timeTo,
                }};
                let eventAdded = false;
                //check if event array not empty
                if(eventsArr.length > 0){{
                    //check if current day has already any event then add to that 
                    eventsArr.forEach((item) => {{
                        if(
                            item.day == activeDay &&
                            item.month == month + 1 &&
                            item.year == year
                        ){{
                            item.events.push(newEvent);
                            eventAdded = true;
                        }}
                    }});
                }}
                //if event array empty or current day has no events create new 
                if(!eventAdded){{
                    eventsArr.push({{
                        day: activeDay,
                        month: month + 1,
                        year: year,
                        events: [newEvent],
                    }});
                }}
                //remove active from add event form
                addEventContainer.classList.remove("active");
                //clear the fields
                addEventTitle.value = "";
                addEventFrom.value = "";
                addEventTo.value = "";
                //show current added event
                updateEvents(activeDay);
                //also add event class to newly added day if not already there
                const activeDayElem = document.querySelector(".day.active");
                if(!activeDayElem.classList.contains("event")){{
                    activeDayElem.classList.add("event");
                }}
            }});

            function convertTime(time){{
                let timeArr = time.split(":");
                let timeHour = timeArr[0];
                let timeMin = timeArr[1];
                let timeFormat = timeHour >= 12 ? "PM" : "AM";
                timeHour = timeHour % 12 || 12;
                time = timeHour + ":" + timeMin + " " + timeFormat;
                return time;
            }}

            //create a function to remove events on click
            eventsContainer.addEventListener("click", (e) => {{
                if(e.target.classList.contains("event")){{
                    const eventTitle = e.target.children[0].children[1].innerHTML;
                    //get the title of event than searn in array by title and delete
                    eventsArr.forEach((event) => {{
                        if(
                            event.day == activeDay &&
                            event.month == month + 1 &&
                            event.year == year
                        ){{
                            event.events.forEach((item , index) => {{
                                if(item.title == eventTitle){{
                                    event.events.splice(index , 1);
                                }}
                            }});
                            //if no events remaining on that day remove complete day
                            if(event.events.length == 0){{
                                eventsArr.splice(eventsArr.indexOf(event) , 1);
                                //after removing complete day also remove active day
                                const activeDayElem = document.querySelector(".day.active");
                                if(activeDayElem.classList.contains("event")){{
                                    activeDayElem.classList.remove("event");
                                }}
                            }}
                        }}
                    }});
                    //after removing array update events
                    updateEvents(activeDay);
                }}
            }});
            









        </script>
        
     """
    return calendarHTML

      
