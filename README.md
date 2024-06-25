<body>
    <h1>Law Firm Management System</h1>
    <p>Welcome to the Law Firm Management System! This project is designed to streamline the operations of a law firm by providing an intuitive platform for managing appointments, lawyers, and blog posts. Built using Django for the backend and HTML, CSS, JavaScript, and Bootstrap for the frontend, this system offers a robust and user-friendly interface for both clients and administrators.</p>
    <h2>Features</h2>
    <h3>Client Features:</h3>
    <ul>
        <li><strong>Landing Page</strong>: A welcoming landing page that provides an overview of the law firm and its services.</li>
        <li><strong>User Authentication</strong>: Secure login system to access personalized dashboard.</li>
        <li><strong>Dashboard</strong>:
            <ul>
                <li>Create and manage their appointments.</li>
                <li>View all available lawyers and their profiles.</li>
                <li>Track the status of their appointments.</li>
            </ul>
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
