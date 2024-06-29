<body>
    <h1>Law Firm Management System</h1>
    <p>Welcome to the Law Firm Management System! This project is designed to streamline the operations of a law firm by providing an intuitive platform for managing appointments, lawyers, and blog posts. Built using Django for the backend and HTML, CSS, JavaScript, and Bootstrap for the frontend, this system offers a robust and user-friendly interface for both clients and administrators.</p>

![Screenshot 2024-06-29 190505](https://github.com/pmammedov/Law-Firm-Project/assets/30790180/3ed52036-ec5a-4bb0-a346-39d3b49468a6)    

![Screenshot 2024-06-29 190824](https://github.com/pmammedov/Law-Firm-Project/assets/30790180/7f293eb9-f24b-4370-83ed-122beb16b30f)
    <h2>Features</h2>
    <h3>Client Features:</h3>
    <ul>
        <li><strong>Landing Page</strong>: A welcoming landing page that provides an overview of the law firm and its services.</li>
        <li><strong>User Authentication</strong>: Secure login system to access personalized dashboard.</li>
        <li><strong>Dashboard</strong>:
            <ul>
        <li>
            <h3>Create and Manage Appointments</h3>
            <p>With our intuitive appointment management system, clients can easily create new appointments, reschedule existing ones, and manage their calendar efficiently. The interface allows for seamless interaction, ensuring that all appointments are organized and easily accessible.</p>
            <img src="https://github.com/pmammedov/Law-Firm-Project/assets/30790180/79ffe97a-33a7-4b2b-9890-274d10bc228a" alt="Create and Manage Appointments">
        </li>
        <li>
            <h3>View All Available Lawyers and Their Profiles</h3>
            <p>Our comprehensive lawyer directory provides clients with detailed profiles of all available lawyers. Each profile includes important information such as areas of expertise, years of experience, and contact details, helping clients make informed decisions when choosing legal representation.</p>
            <img src="https://github.com/pmammedov/Law-Firm-Project/assets/30790180/e9f85f92-d64b-4322-b824-79706240b1fc" alt="View All Available Lawyers and Their Profiles">
        </li>
        <li>
            <h3>Track the Status of Their Appointments</h3>
            <p>Our appointment tracking feature keeps clients informed about the status of their appointments. Clients can easily see upcoming appointments, receive reminders, and get updates on any changes, ensuring they are always in the loop.</p>
        </li>
        <li>
            <h3>Create and Manage Your Blogs</h3>
            <p>Our blogging platform allows users to create and manage their blogs effortlessly. Share insights, updates, and legal news with the community. The user-friendly interface makes it easy to format and publish content.</p>
            <img src="https://github.com/pmammedov/Law-Firm-Project/assets/30790180/a2fb87fd-a74f-4f38-93ec-73baacf40d64" alt="Create and Manage Your Blogs">
        </li>
        <li>
            <h3>Make Comments on Blogs</h3>
            <p>Engage with the community by commenting on blog posts. Our commenting system allows users to share their thoughts, ask questions, and interact with blog authors and other readers, fostering a vibrant and interactive community.</p>
            <img src="https://github.com/pmammedov/Law-Firm-Project/assets/30790180/390674ee-d51b-430c-a67b-2b028b21b71a" alt="Make Comments on Blogs">
        </li>
    </ul>
    <h3>Admin Features:</h3>
    <ul>
        <li><strong>CRUD Operations</strong>: Admins have full control over:
            <ul>
                <li><strong>Blogs</strong>: Create, read, update, and delete blog posts to keep the content fresh and informative.</li>
                <li><strong>Appointments</strong>: Manage all appointments, including creating, updating, and deleting them as necessary.</li>
                <li><strong>Lawyers</strong>: Maintain the list of lawyers by adding, updating, or removing their profiles.</li>
            </ul>
        </li>
    </ul>
    <h2>Technologies Used</h2>
    <h3>Backend:</h3>
    <ul>
        <li><strong>Django</strong>: A high-level Python web framework that encourages rapid development and clean, pragmatic design.</li>
    </ul>
    <h3>Frontend:</h3>
    <ul>
        <li><strong>HTML5</strong>: Markup language used for structuring and presenting content.</li>
        <li><strong>CSS3</strong>: Stylesheet language used for describing the presentation of a document written in HTML.</li>
        <li><strong>JavaScript</strong>: Programming language used to create dynamic and interactive effects within web browsers.</li>
        <li><strong>Bootstrap</strong>: Frontend component library for developing responsive and mobile-first websites.</li>
    </ul>
    <h2>Installation</h2>
    <p>To get a local copy up and running follow these simple steps:</p>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone git@github.com:pmammedov/Law-Firm-Project.git</code></pre>
        </li>
        <li><strong>Navigate to the project directory:</strong>
            <pre><code>cd Law-Firm-Project</code></pre>
        </li>
        <li><strong>Create a virtual environment:</strong>
            <pre><code>python -m venv env</code></pre>
        </li>
        <li><strong>Activate the virtual environment:</strong>
            <ul>
                <li>On Windows:
                    <pre><code>.\env\Scripts\activate</code></pre>
                </li>
                <li>On macOS and Linux:
                    <pre><code>source env/bin/activate</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Install dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Apply migrations:</strong>
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li><strong>Create a superuser:</strong>
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li><strong>Run the server:</strong>
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the application:</strong>
            <p>Open your web browser and go to <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>.</p>
        </li>
    </ol>
    <h2>Usage</h2>
    <h3>For Clients:</h3>
    <ol>
        <li>Visit the landing page and log in with your credentials.</li>
        <li>Navigate to your dashboard to create and manage appointments.</li>
        <li>View lawyer profiles and track the status of your appointments.</li>
    </ol>
    <h3>For Admins:</h3>
    <ol>
        <li>Log in with your admin credentials.</li>
        <li>Access the admin panel to manage blogs, appointments, and lawyer profiles through the CRUD interface.</li>
    </ol>
    <h2>Contact</h2>
    <p><a href="mailto:pmammedov@gmail.com">MailToMe</a></p>
    <p>Thank you for visiting! If you find this project helpful, please give it a star 🌟.</p>
</body>
