import psutil

class DrivesInfo:
    @staticmethod
    def print():
        drives = psutil.disk_partitions()

        for drive in drives:
            print(f"Name: {drive.device}")
            print(f"Type: {drive.fstype}")
            try:
                drive_usage = psutil.disk_usage(drive.mountpoint)
            except PermissionError:
                print("Access denied")
            total_size = drive_usage.total
            free_space = drive_usage.free
            print(f"Capacity: {total_size}")
            print(f"Free space: {free_space}")
            percentage = drive_usage.percent
            print(f"Percentage: {percentage}")
    
            print()