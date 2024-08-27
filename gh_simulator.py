import sys

def simulate_gh_command(command):
    commands = {
        "gh --version": "gh version 2.32.1 (2024-08-27)",
        "gh auth login": "Logged in as user@example.com",
        "gh repo create": "✓ Created repository 'user/repo' on GitHub\n✓ Added remote https://github.com/user/repo.git",
        "gh repo clone user/repo": "Cloning into 'repo'...\ndone.",
        "gh issue list": "Showing 3 open issues in user/repo\n\n#1  Issue title one\n#2  Issue title two\n#3  Issue title three",
        "gh pr list": "Showing 2 open pull requests in user/repo\n\n#12  PR title one\n#34  PR title two"
    }

    if command in commands:
        print(commands[command])
    else:
        print(f"Unknown command: {command}")
        print("Use 'gh --help' for a list of available commands.")

def main():
    if len(sys.argv) > 1:
        command = ' '.join(sys.argv[1:])
        simulate_gh_command(command)
    else:
        print("Usage: python gh_simulator.py <command>")

if __name__ == "__main__":
    main()
