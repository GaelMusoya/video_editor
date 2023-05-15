from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

def process_video(video_path, dst):
    # Load the video file
    clip = VideoFileClip(video_path)
    # Remove audio
    clip = clip.without_audio()
    
    # Get the full duration of the clip
    full_duration = clip.duration

    # Define the angles and speeds
    angles_speeds = [(0, 360, 1.0), (270, 360, -1.0), (90, 270, -2.0), (0, 90, -0.5)]
    
    # Process each angle-speed pair
    processed_clips = []
    for start_angle, end_angle, speed in angles_speeds:
        # Convert angles to times
        start_time = full_duration * (start_angle / 360)
        end_time = full_duration * (end_angle / 360)
        
        # Extract the subclip
        subclip = clip.subclip(start_time, end_time)
        
        # Change the speed
        if speed < 0:
            subclip = vfx.time_mirror(subclip)
            subclip = vfx.speedx(subclip, -speed)
        else:
            subclip = vfx.speedx(subclip, speed)
        
        processed_clips.append(subclip)

    # Concatenate the processed clips
    final_clip = concatenate_videoclips(processed_clips)
    
    # Write the final clip to a file
    final_clip.write_videofile(dst, codec='libx264')


src = 'data/Adam Revolved.mp4'
dst = 'data/output.mp4'

process_video(src, dst)