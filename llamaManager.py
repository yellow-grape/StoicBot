import subprocess

class OllamaManager:
    def __init__(self):
        self.container_name = 'ollama_container'

    def start_ollama_container(self):
        """Starts the Ollama Docker container."""
        subprocess.run(['docker', 'run', '-d', '--name', self.container_name, 'ollama'])
        print(f'Ollama container {self.container_name} started.')

    def stop_ollama_container(self):
        """Stops the Ollama Docker container."""
        subprocess.run(['docker', 'stop', self.container_name])
        subprocess.run(['docker', 'rm', self.container_name])
        print(f'Ollama container {self.container_name} stopped and removed.')

    def send_prompt(self, prompt: str):
        """Sends a prompt to the Ollama container and returns the response."""
        result = subprocess.run(['docker', 'exec', self.container_name, 'ollama', 'send', prompt], capture_output=True, text=True)
        return result.stdout.strip()

    def format_response(self, response: str):
        """Formats the response for further use."""
        return {'response': response}

# Example usage
if __name__ == '__main__':
    manager = OllamaManager()
    manager.start_ollama_container()
    response = manager.send_prompt('Hello, Ollama!')
    formatted_response = manager.format_response(response)
    print(formatted_response)