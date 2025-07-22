With the exponential growth in cloud storage usage, ensuring secure and efficient access control for shared data has become a critical concern. Traditional encryption schemes fall short when it comes to group-based access where data must be securely shared among a dynamic set of users. This project proposes a Group Key Management Protocol (GKMP) that allows secure, scalable, and efficient file sharing on cloud platforms by managing encryption keys for a group of users in a dynamic and decentralized manner.

To design and implement a secure group key management protocol that:

Allows encrypted file sharing among a group of authorized users.

Supports user join and leave operations efficiently.

Minimizes communication and computation overhead.

Ensures forward and backward secrecy.

Can be integrated with cloud-based file storage services (e.g., AWS S3, Google Drive, Azure Blob, etc.).


Key Features:
Group Key Generation: A central authority (or decentralized model) generates a symmetric group key that is used to encrypt/decrypt shared files.

User Join/Leave Protocols: Efficient re-keying mechanism when users are added or removed, without requiring full key redistribution.

Forward Secrecy: A user who leaves the group cannot access future files.

Backward Secrecy: A user who joins the group cannot access previously shared files.

Access Control: Role-based or policy-based access control ensures only authorized users get the group key.

Cloud Integration: Encrypted files are stored on the cloud and can be accessed/decrypted only using valid group keys.

 System Architecture:
User Interface (Web or CLI):

Upload/download files

Manage group membership

View shared files

Key Management Server:

Handles key generation, distribution, and re-keying.

Maintains access logs and group metadata.

Cloud Storage:

Stores encrypted files.

Handles standard storage operations like versioning, access logs, etc.

Client Application:

Encrypts/decrypts files using the group key.

Communicates with both the key server and the cloud provider.

🧪 Use Cases:
Secure document collaboration among multiple team members.

Academic or research groups sharing sensitive data.

Healthcare data sharing among authorized personnel.

Enterprise environments where departments need encrypted shared access.



