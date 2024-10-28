#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string loadShaderSource(const char* filePath) {
	ifstream file(filePath);
	stringstream buffer;
	buffer << file.rdbuf();
	return buffer.str();
}

GLuint compileShader(const char* source, GLenum shaderType) {
	GLuint shader = glCreateShader(shaderType);
	glShaderSource(shader, 1, &source, nullptr);
	glCompileShader(shader);

	GLint success;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
	if (!success) {
		GLchar infoLog[512];
		glGetProgramInfoLog(shader, 512, nullptr, infoLog);
		cout << "Shader compilation failed: " << infoLog << endl;
	}
	return shader;
}

GLuint createShaderProgram(const char* vertexPath, const char* fragmentPath) {
	string vertexCode = loadShaderSource(vertexPath);
	string fragmentCode = loadShaderSource(fragmentPath);

	GLuint vertexShader = compileShader(vertexCode.c_str(), GL_VERTEX_SHADER);
	GLuint fragmentShader = compileShader(fragmentCode.c_str(), GL_FRAGMENT_SHADER);

	GLuint shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);

	GLint success;
	glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
	if (!success) {
		GLchar infoLog[512];
		glGetProgramInfoLog(shaderProgram, 512, nullptr, infoLog);
		cout << "Shader program linking failed: " << infoLog << endl;
	}

	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);

	return shaderProgram;
}

// Fonctions pour charger et compiler les shaders (déjà expliquées précédemment)
std::string loadShaderSource(const char* filePath);
GLuint compileShader(const char* source, GLenum shaderType);
GLuint createShaderProgram(const char* vertexPath, const char* fragmentPath);

int main() {
    // Initialiser GLFW
    if (!glfwInit()) {
        std::cerr << "Erreur lors de l'initialisation de GLFW" << std::endl;
        return -1;
    }

    // Configurer la version d'OpenGL et le profil
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // Créer la fenêtre GLFW
    GLFWwindow* window = glfwCreateWindow(800, 600, "Triangle avec Shaders", nullptr, nullptr);
    if (!window) {
        std::cerr << "Erreur lors de la création de la fenêtre GLFW" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // Initialiser GLEW
    if (glewInit() != GLEW_OK) {
        std::cerr << "Erreur lors de l'initialisation de GLEW" << std::endl;
        return -1;
    }

    // Définir le viewport
    glViewport(0, 0, 800, 600);

    // Définir les sommets d'un triangle
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, // Bas gauche
         0.5f, -0.5f, 0.0f, // Bas droit
         0.0f,  0.5f, 0.0f  // Haut
    };

    // Créer le VAO et le VBO
    unsigned int VAO, VBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    // Lier le VAO
    glBindVertexArray(VAO);

    // Lier et remplir le VBO avec les données des sommets
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // Configurer l'attribut des sommets
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    // Créer les shaders et le programme de shader
    GLuint shaderProgram = createShaderProgram("vertex_shader.glsl", "fragment_shader.glsl");

    // Boucle de rendu
    while (!glfwWindowShouldClose(window)) {
        // Gérer les événements
        glfwPollEvents();

        // Effacer le tampon de couleur
        glClear(GL_COLOR_BUFFER_BIT);

        // Utiliser le programme de shader
        glUseProgram(shaderProgram);

        // Dessiner le triangle
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        // Échanger les tampons
        glfwSwapBuffers(window);
    }

    // Nettoyer
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    // Terminer GLFW
    glfwTerminate();
    return 0;
}
