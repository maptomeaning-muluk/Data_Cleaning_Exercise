# import os
# import shutil
# import glob
#
#
# # Function to create the new dataset folder with the desired structure
# def create_dataset(source_dir, target_dir):
#     # Extract folder name from the source directory
#     folder_name = os.path.basename(source_dir)
#
#     # Define paths for Label, Before, and After folders
#     label_folder = os.path.join(source_dir, 'Label')
#     before_folder = os.path.join(source_dir, 'Before')
#     after_folder = os.path.join(source_dir, 'After')
#
#     # Create target folder structure
#     target_folder = os.path.join(target_dir, folder_name)
#     target_label_folder = os.path.join(target_folder, 'Label')
#     target_before_folder = os.path.join(target_folder, 'Before')
#     target_after_folder = os.path.join(target_folder, 'After')
#
#     os.makedirs(target_label_folder, exist_ok=True)
#     os.makedirs(target_before_folder, exist_ok=True)
#     os.makedirs(target_after_folder, exist_ok=True)
#
#     # Process files in the Label folder
#     label_files = glob.glob(os.path.join(label_folder, '*.csv'))
#     print(f"Found {len(label_files)} label CSV files in {label_folder}")
#
#     for label_file in label_files:
#         # Extract base name without extension
#         base_name = os.path.splitext(os.path.basename(label_file))[0]
#
#         # Extract the required part "2019_01_mosaic_L15-1848E-0793N_7394_5018_13"
#         required_part = '_'.join(base_name.split('_')[2:])
#
#         # Find corresponding Before and After files based on the required part
#         before_file_pattern = os.path.join(before_folder, f'*{required_part}.tif')
#         after_file_pattern = os.path.join(after_folder, f'*{required_part}.tif')
#
#         # Check if Before and After files exist
#         before_files = glob.glob(before_file_pattern)
#         after_files = glob.glob(after_file_pattern)
#
#         if before_files and after_files:
#             # Since there might be multiple matches, choose the first one
#             before_file = before_files[0]
#             after_file = after_files[0]
#
#             # Copy files to target folders with the new names
#             shutil.copy(label_file, os.path.join(target_label_folder, f"{required_part}.csv"))
#             shutil.copy(before_file, os.path.join(target_before_folder, f"{required_part}.tif"))
#             shutil.copy(after_file, os.path.join(target_after_folder, f"{required_part}.tif"))
#
#             print(f"Copied {label_file} to {os.path.join(target_label_folder, f'{required_part}.csv')}")
#             print(f"Copied {before_file} to {os.path.join(target_before_folder, f'{required_part}.tif')}")
#             print(f"Copied {after_file} to {os.path.join(target_after_folder, f'{required_part}.tif')}")
#
#         else:
#             print(f"No matching Before or After files found for {base_name} in {before_folder} or {after_folder}")
#
#
# # Define the base directory where your source folders are located
# source_base_path = r"D:\SpatialHawk\Kaggle\!!!!!!!!Final_Data_Test\Change_Detection"
# target_base_path = r"D:\SpatialHawk\Kaggle\!!!!!!!!Final_Data_Test\New_Output"
#
# # List all folders in the source base directory
# folder_list = os.listdir(source_base_path)
#
# # Process each folder in the list
# for folder_name in folder_list:
#     source_folder = os.path.join(source_base_path, folder_name)
#     create_dataset(source_folder, target_base_path)


import os
import shutil
import glob

# Function to create the new dataset folder with the desired structure
def create_dataset(source_dir, target_dir):
    # Extract folder name from the source directory
    folder_name = os.path.basename(source_dir)

    # Define paths for Label, Before, and After folders
    label_folder = os.path.join(source_dir, 'Label')
    before_folder = os.path.join(source_dir, 'Before')
    after_folder = os.path.join(source_dir, 'After')

    # Create target folder structure
    target_folder = os.path.join(target_dir, folder_name)
    target_label_folder = os.path.join(target_folder, 'Label')
    target_before_folder = os.path.join(target_folder, 'Before')
    target_after_folder = os.path.join(target_folder, 'After')

    os.makedirs(target_label_folder, exist_ok=True)
    os.makedirs(target_before_folder, exist_ok=True)
    os.makedirs(target_after_folder, exist_ok=True)

    # Process files in the Label folder
    label_files = glob.glob(os.path.join(label_folder, '*.csv'))
    print(f"Found {len(label_files)} label CSV files in {label_folder}")

    for label_file in label_files:
        # Extract base name without extension
        base_name = os.path.splitext(os.path.basename(label_file))[0]

        # Extract the required part "2019_01_mosaic_L15-1848E-0793N_7394_5018_13"
        required_part = '_'.join(base_name.split('_')[2:])

        # Find corresponding Before and After files based on the required part
        before_file_pattern = os.path.join(before_folder, f'*{required_part}.tif')
        after_file_pattern = os.path.join(after_folder, f'*{required_part}.tif')

        # Check if Before and After files exist
        before_files = glob.glob(before_file_pattern)
        after_files = glob.glob(after_file_pattern)

        if before_files and after_files:
            # Since there might be multiple matches, choose the first one
            before_file = before_files[0]
            after_file = after_files[0]

            # Copy files to target folders with the new names
            shutil.copy(label_file, os.path.join(target_label_folder, f"{required_part}.csv"))
            shutil.copy(before_file, os.path.join(target_before_folder, f"{required_part}.tif"))
            shutil.copy(after_file, os.path.join(target_after_folder, f"{required_part}.tif"))

            print(f"Copied {label_file} to {os.path.join(target_label_folder, f'{required_part}.csv')}")
            print(f"Copied {before_file} to {os.path.join(target_before_folder, f'{required_part}.tif')}")
            print(f"Copied {after_file} to {os.path.join(target_after_folder, f'{required_part}.tif')}")

        else:
            print(f"No matching Before or After files found for {base_name} in {before_folder} or {after_folder}")


# Define the base directory where your source folders are located
source_base_path = r"D:\SpatialHawk\Kaggle\!!!!!!!!Final_Data_Test\Change_Detection"
target_base_path = r"D:\SpatialHawk\Kaggle\!!!!!!!!Final_Data_Test\New_Output"

# List of folders to process
folder_list = [
    "L15-0331E-1257N_1327_3160_13",
    "L15-0357E-1223N_1429_3296_13",
    "L15-0358E-1220N_1433_3310_13",
    "L15-0361E-1300N_1446_2989_13",
    "L15-0368E-1245N_1474_3210_13",
    "L15-0387E-1276N_1549_3087_13",
    "L15-0434E-1218N_1736_3318_13",
    "L15-0457E-1135N_1831_3648_13",
    "L15-0487E-1246N_1950_3207_13",
    "L15-0506E-1204N_2027_3374_13",
    "L15-0544E-1228N_2176_3279_13",
    "L15-0566E-1185N_2265_3451_13",
    "L15-0571E-1075N_2287_3888_13",
    "L15-0577E-1243N_2309_3217_13",
    "L15-0586E-1127N_2345_3680_13",
    "L15-0595E-1278N_2383_3079_13",
    "L15-0614E-0946N_2459_4406_13",
    "L15-0632E-0892N_2528_4620_13",
    "L15-0683E-1006N_2732_4164_13",
    "L15-0760E-0887N_3041_4643_13",
    "L15-0924E-1108N_3699_3757_13",
    "L15-0977E-1187N_3911_3441_13",
    "L15-1014E-1375N_4056_2688_13",
    "L15-1015E-1062N_4061_3941_13",
    "L15-1025E-1366N_4102_2726_13",
    "L15-1049E-1370N_4196_2710_13",
    "L15-1138E-1216N_4553_3325_13",
    "L15-1172E-1306N_4688_2967_13",
    "L15-1185E-0935N_4742_4450_13",
    "L15-1200E-0847N_4802_4803_13",
    "L15-1203E-1203N_4815_3378_13",
    "L15-1204E-1202N_4816_3380_13",
    "L15-1204E-1204N_4819_3372_13",
    "L15-1209E-1113N_4838_3737_13",
    "L15-1210E-1025N_4840_4088_13",
    "L15-1276E-1107N_5105_3761_13",
    "L15-1289E-1169N_5156_3514_13",
    "L15-1296E-1198N_5184_3399_13",
    "L15-1298E-1322N_5193_2903_13",
    "L15-1335E-1166N_5342_3524_13",
    "L15-1389E-1284N_5557_3054_13",
    "L15-1438E-1134N_5753_3655_13",
    "L15-1439E-1134N_5759_3655_13",
    "L15-1479E-1101N_5916_3785_13",
    "L15-1481E-1119N_5927_3715_13",
    "L15-1538E-1163N_6154_3539_13",
    "L15-1615E-1205N_6460_3370_13",
    "L15-1615E-1206N_6460_3366_13",
    "L15-1617E-1207N_6468_3360_13",
    "L15-1669E-1153N_6678_3579_13",
    "L15-1669E-1160N_6678_3548_13",
    "L15-1669E-1160N_6679_3549_13",
    "L15-1672E-1207N_6691_3363_13",
    "L15-1690E-1211N_6763_3346_13",
    "L15-1691E-1211N_6764_3347_13",
    "L15-1703E-1219N_6813_3313_13",
    "L15-1709E-1112N_6838_3742_13",
    "L15-1716E-1211N_6864_3345_13",
    "L15-1748E-1247N_6993_3202_13",
    "L15-1848E-0793N_7394_5018_13"
]

# Process each folder in the list
for folder_name in folder_list:
    source_folder = os.path.join(source_base_path, folder_name)
    create_dataset(source_folder, target_base_path)

